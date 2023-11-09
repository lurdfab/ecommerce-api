from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import filters


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    # @action(detail=True, methods=['POST'])
    # def create_size_variant(self, request, *args, **kwargs):
    #     self.object = get_object_or_404(self.get_queryset(), **kwargs)
    #     serializer =SizeVariantSerializer(data=request.data)
        
    #     if not serializer.is_valid():
    #         raise Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    #     variant = serializer.save(product=self.object)
    #     print(variant.product.id)
    #     data = ProductSerializer(variant.product).data
    #     return Response(data, status=status.HTTP_200_OK)
        
    
    # def get_serializer(self, *args, **kwargs):
    #     if self.action == 'create_size_variant':
    #         self.serializer_class = SizeVariantSerializer()
    #     else:
    #         self.serializer_class = ProductSerializer()

    #     return self.serializer_class


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

class ProductSearchViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'brand', 'category']
