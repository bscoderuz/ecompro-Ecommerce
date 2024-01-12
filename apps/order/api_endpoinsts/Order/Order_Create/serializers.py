from rest_framework.serializers import ModelSerializer

from apps.order.models.models import Order


class OrderCreateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'full_name',
            'phone_number',
            'email',
            'product',
            'delivery_type',
            'payment_method',
            'city',
            'region',
            'address',
            'level',
            'delivery_date',
        ]
