from django.db.models import Sum, ExpressionWrapper, IntegerField
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from supplai_api.apps.transaction.models import Transaction
from supplai_api.apps.transaction.api.serializers import (
    TransactionSerializer, TransactionBalanceSerializer
)


class BaseTransactionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class NewTransactionViewSet(BaseTransactionViewSet, mixins.CreateModelMixin):
    pass


class TransactionStatementViewSet(BaseTransactionViewSet, mixins.RetrieveModelMixin):
    def get_queryset(self):
        queryset = self.queryset
        user_id = self.kwargs.get('pk')

        if user_id:
            queryset = queryset.filter(user=user_id).order_by('-created_at').distinct()

        return queryset

    def retrieve(self, *args, **kwargs):
        transactions = self.get_queryset()
        serialized_transactions = self.serializer_class(transactions, many=True)
        return Response(serialized_transactions.data)


class TransactionBalanceViewSet(BaseTransactionViewSet, mixins.RetrieveModelMixin):
    def get_queryset(self):
        queryset = self.queryset
        user_id = self.kwargs.get('pk')

        if user_id:
            user_statement = queryset.filter(user=user_id)
            if user_statement:
                incomes = user_statement.filter(type='e').aggregate(result=Sum('value')).get('result')
                withdraws = user_statement.filter(type='s').aggregate(result=Sum('value')).get('result')
                balance = incomes - withdraws if incomes or withdraws else 0
                queryset = {'balance': balance}

        return queryset

    def retrieve(self, *args, **kwargs):
       balance = self.get_queryset()
       print(balance)
       return Response(balance)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TransactionBalanceSerializer
