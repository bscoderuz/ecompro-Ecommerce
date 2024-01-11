from rest_framework import generics
from .serializers import ProductRetrieveSerializer
from apps.product.models.models import Product


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductRetrieveSerializer
    queryset = Product.objects.filter(active=True)


__all__ = ['ProductRetrieveAPIView']
