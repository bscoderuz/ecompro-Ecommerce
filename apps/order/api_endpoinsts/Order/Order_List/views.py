from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.order.models.models import Order
from .serializers import OrderListSerializer


class OrderListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderListSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


__all__ = ['OrderListAPIView']
