from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from orders.models import Order


class PaymentViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get_queryset(self):
        id=self.kwargs['id']
        qs = super().get_queryset()
        qs.filter(user=self.request.user, order=id)
        return qs
    
    def perform_create(self, serializer):
        id=self.kwargs['id']
        order = Order.objects.get(id=id)
        obj = serializer.save(user=self.request.user, order=order)
        
        if obj.payment_type =="cash":
            pass
        elif obj.payment_type =="paypal":
            link = obj.create_payment()
            return Response({"link":link}, status=status.HTTP_201_CREATED)

        elif obj.payment_type =="cc":
            pass
        elif obj.payment_type =="transfer":
            pass


    @action(detail=True, methods=['POST'])
    def paypal_cancel(self, request, *args, **kwargs):
        id=self.kwargs['id']
        qs = super().get_queryset()
        qs = qs.filter(order=id)
        qs.status = 2
        qs.save()
        return Response(status = status.HTTP_200_OK )
    
    @action(detail=True, methods=['POST'])
    def paypal_success(self, request, *args, **kwargs):
        id=self.kwargs['id']
        qs = super().get_queryset()
        qs = qs.filter(order=id)
        qs.status = 1
        qs.save()
        return Response(status = status.HTTP_200_OK )
    

