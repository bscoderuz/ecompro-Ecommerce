from rest_framework import generics
from apps.cart.models import Cart, CartItem
from .serializers import CartItemSerializer


class CartItemListAPIView(generics.ListAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        cart_id = self.kwargs.get('cart_id')
        return CartItem.objects.filter(cart__id=cart_id)


__all__ = ['CartItemListAPIView']
