from rest_framework.serializers import ModelSerializer
from .models import TRANSACTIONS_TYPE, Transactions


class TransactionSerializer(ModelSerializer):

    type = ModelSerializer.CharField(choices=TRANSACTIONS_TYPE)

    class Meta:
        model = Transactions
        fields = ["id", "type", "date", "value", "cpf", "card", "hour", "owner_store", "name_store"]

        def create(self, validated_data: dict) -> Transactions:
            return Transactions.objects.create(**validated_data)