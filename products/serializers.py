from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"



class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = "__all__"

# class SizeVariantSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SizeVariant
#         fields = '__all__'
#         read_only_fields = ("product",)


# class ColorVariantSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ColorVariant
#         fields = '__all__'
#         read_only_fields = ("product",)

class ProductSerializer(serializers.ModelSerializer):
    # a = serializers.SerializerMethodField()
    # b = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("id", "category", "name", "description", "price", "image", "stock", "brand")
        read_only_fields = ("owner",)

    # def get_a(self, obj):
    #     if hasattr(obj, "sizes"):
    #         return SizeVariantSerializer(obj.sizes, many=True).data
    #     return None
    
    # def get_b(self, obj):
    #     if hasattr(obj, "colors"):
    #         return ColorVariantSerializer(obj.colors, many=True).data
    #     return None

    

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ("owner",)



