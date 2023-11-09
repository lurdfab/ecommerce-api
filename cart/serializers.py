from rest_framework import serializers
from .models import *


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ("id","quantity", "product")

class WishListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WishList
        fields = ("id", "product")