from rest_framework import generics

from apps.product.models import Category
from .serializers import CategoryListSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


__all__ = ["CategoryListAPIView"]
