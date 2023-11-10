from rest_framework import serializers
from .models import *
from products.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):

    items = serializers.SerializerMethodField()
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ("user", "order_date", 'name', 'phone_number', 'address', 'town', 'state', 'zipcode', 'country', 'delivery', "items", "coupon", "total_amount")
        read_only_fields = ("user",)
    

    def get_items(self, obj):
        data = OrderItem.objects.filter(order=obj)
        return OrderItemSerializer(data, many=True).data


    def get_total_amount(self, obj):
        return obj.get_total_amount()


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = "__all__"

