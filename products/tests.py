""" Tests for Product """

from django.test import TestCase

from .models import Product
from .models import Category


class ProductModelTests(TestCase):
    """ Unit test class for Product model """
    def setUp(self):

        """ Create category and product for the testing """
        Category.objects.create(
            name="animanl_parts", friendly_name="Animal parts"
        )

        Product.objects.create(
            name="Minifig accessory shield ovoid with dragon\
                 blue and red pattern",
            sku="770p4c",
            description="Shield whit a dragon on",
            price=12.0,
        )

    def test_was_category_inserted(self):
        """
        test_was_category_inserted() returns False for if category not inserted
        """
        category = Category.objects.get(name="animanl_parts")
        self.assertEqual(category.friendly_name, "Animal parts")

    def test_was_product_inserted(self):
        """
        test_was_product_inserted() returns False for if category not inserted
        """
        product = Product.objects.get(sku="770p4c")
        print(f"A: {product}")
        self.assertEqual(
            product.description,
            "Shield whit a dragon on",
        )
