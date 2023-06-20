""" Tests for Product """

from django.test import TestCase

from .models import Product
from .models import Category


class ProductModelTests(TestCase):
    def setUp(self):
        Category.objects.create(name="heads", friendly_name="Heads")
        Category.objects.create(name="bricks", friendly_name="Bricks")

        Product.objects.create(name="red_head", sku="123-1231", description="Red lego head", price=12.0)
        Product.objects.create(name="blue_head", sku="123-122131", description="Blue lego head", price=12.0)

    def test_was_category_inserted(self):
        """
        test_was_category_inserted() returns False for if category not inserted
        """

        self.assertIs(Category.objects.get(name="heads"), False)

    def test_was_product_inserted(self):
        """
        test_was_product_inserted() returns False for if category not inserted
        """

        self.assertIs(Product.objects.get(name="blue_head"), False)
