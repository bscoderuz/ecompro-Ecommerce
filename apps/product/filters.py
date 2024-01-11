import django_filters
from apps.product.models.models import Product


class ProductCustomFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'price': ['exact', 'gte', 'lte'],
            'category': ['exact'],
        }
