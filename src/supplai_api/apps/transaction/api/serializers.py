from rest_framework import serializers

from supplai_api.apps.transaction.models import Transaction
from supplai_api.apps.core.api.serializers import UserSerializer


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('type', 'value', 'user', 'created_at')


class TransactionBalanceSerializer(serializers.Serializer):
    balance = serializers.DecimalField(max_digits=10, decimal_places=2)


class UserDetailSerializer(serializers.Serializer):
    # balance = TransactionBalanceSerializer(many=True, read_only=True)
    # statement = TransactionSerializer(many=True, read_only=True)
    user = UserSerializer()

    class Meta:
        fields = ('user',)
