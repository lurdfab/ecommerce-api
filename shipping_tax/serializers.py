from rest_framework import serializers
from .models import Shipping, Tax

class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = ('name', 'phone_number', 'address', 'town', 'state', 'zipcode', 'country', 'delivery', 'amount')

# class TaxSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tax
#         fields = ('id', 'name', 'rate')