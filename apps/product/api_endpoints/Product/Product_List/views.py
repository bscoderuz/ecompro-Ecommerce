from rest_framework import generics

from apps.product.filters import ProductCustomFilter
from apps.product.models import Product
from .serializers import ProductListSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.prefetch_related('images').filter(active=True)
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductCustomFilter
