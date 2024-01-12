from rest_framework import generics, serializers
from rest_framework.response import Response

from apps.cart.models import Cart
from .serializers import CartItemSerializer


class CartItemCreateAPIView(generics.CreateAPIView):
    serializer_class = CartItemSerializer

    def perform_create(self, serializer):
        cart_id = self.kwargs.get('cart_id')
        cart = Cart.objects.get(id=cart_id)
        serializer.save(cart=cart)
