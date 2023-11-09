from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_class = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
        


