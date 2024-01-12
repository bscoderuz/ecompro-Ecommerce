from django.test import TestCase
from apps.product.models import Category, Product, ProductImage


class ProductModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Electronics',
            description='Electronic products'
        )

        self.product = Product.objects.create(
            name='Smartphone',
            description='High-end smartphone',
            price=999.99,
            category=self.category,
            active=True
        )

        self.product_image = ProductImage.objects.create(
            product=self.product,
            image='product_images/test_image.jpg'
        )

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Electronics')

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Smartphone-999.99')

    def test_product_image_str(self):
        self.assertEqual(str(self.product_image), 'Smartphone-product_images/test_image.jpg')

    def test_product_image_upload_to(self):
        upload_to = ProductImage._meta.get_field('image').upload_to(self.product_image, 'test_image.jpg')
        expected_upload_path = 'product_images/test_image.jpg'
        self.assertEqual(upload_to, expected_upload_path)
