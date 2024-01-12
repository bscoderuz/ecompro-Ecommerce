from rest_framework import generics
from rest_framework.response import Response
from apps.cart.models import CartItem
from .serializers import CartItemSerializer


class CartItemDeleteAPIView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {
                "status": True,
                "message": "Cart item deleted successfully."
            }
        )
