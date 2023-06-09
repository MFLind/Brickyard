""" Model for Products """
from django.db import models


class Category(models.Model):
    """Category model"""

    class Meta:
        """Meta class"""

        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """string return of name"""
        return str(self.name)

    def get_friendly_name(self):
        """Return friendly name"""
        return self.friendly_name


class Product(models.Model):
    """Product model"""

    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """string return of name"""
        return str(self.name)
