from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from apps.order.models.models import Order, OrderItem
from .serializers import OrderSerializer


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


__all__ = ["OrderCreateAPIView"]
