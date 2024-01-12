from rest_framework import generics
from apps.cart.models import CartItem
from .serializers import CartItemSerializer


class CartItemUpdateView(generics.UpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
