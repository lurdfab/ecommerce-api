from rest_framework import serializers
from .models import *


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ("user", "order", "timestamp", "status", "payment_type", "description")
        read_only_fields = ("user", "order", "timestamp", "status",)
