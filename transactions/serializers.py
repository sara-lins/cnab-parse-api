from rest_framework import serializers
from datetime import date, time
from .models import TRANSACTIONS_TYPE, Transactions
import ipdb

class TransactionSerializer(serializers.ModelSerializer):

    value = serializers.CharField(max_length=10)

    class Meta:
        model = Transactions
        fields = ["id", "type", "date", "value", "cpf", "card", "hour", "owner_store", "name_store"]

    def create(self, validated_data: dict) -> Transactions:

        value = validated_data.pop("value")
        validated_data["value"] = int(value) / 100.00

        date_att = validated_data.pop("date")
        year = date_att.year
        month = date_att.month
        day = date_att.day

        new_date = date(year, month, day)
        validated_data["date"] = new_date

        hour_att = validated_data.pop("hour")
        hour =hour_att.hour
        min = hour_att.minute
        sec = hour_att.second

        new_hour = time(hour, min, sec)
        validated_data["hour"] = new_hour

        type_transaction = validated_data.pop("type")

        for key, type in TRANSACTIONS_TYPE.items():
            if key == type_transaction:
                validated_data["type"] = type

        return Transactions.objects.create(**validated_data)