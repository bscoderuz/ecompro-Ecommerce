from django.db import models
from apps.common.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}-{self.price}"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductImage(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"{self.product}-{self.image}"

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"
