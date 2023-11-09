from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets, mixins
from cart.models import Cart
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#this only creates & lists the order and delete the cart after the order is done
class OrderViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        carts = Cart.objects.filter(user=self.request.user)
        if carts.count()>0:
            order = serializer.save(user=self.request.user)
            for cart in carts:
                 OrderItem.objects.create(product=cart.product, order=order, quantity=cart.quantity)
                 cart.delete()





       
        

        

    
 


