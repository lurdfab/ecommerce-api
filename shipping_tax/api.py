from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Shipping, Tax
from .serializers import ShippingSerializer, TaxSerializer

class ShippingTaxViewSet(viewsets.ModelViewSet):
    
    def get(self, request, *args, **kwargs):
        shipping = Shipping.objects.all()
        tax = Tax.objects.all()

        shipping_serializer = ShippingSerializer(shipping, many=True)
        tax_serializer = TaxSerializer(tax, many=True)

        data = {
            'shipping_rates': shipping_serializer.data,
            'tax_rates': tax_serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)

