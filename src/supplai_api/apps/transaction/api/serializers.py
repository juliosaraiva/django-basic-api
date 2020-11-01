from rest_framework import serializers

from supplai_api.apps.transaction.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('type', 'value', 'user', 'created_at')


class TransactionBalanceSerializer(serializers.Serializer):
    balance = serializers.DecimalField(max_digits=10, decimal_places=2)
