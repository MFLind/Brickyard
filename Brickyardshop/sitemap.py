""" Sitemap.xml handler """
from django.contrib import sitemaps
from django.urls import reverse
from products.models import Product, Category


class ProductSitemap(sitemaps.Sitemap):
    """Product sitesmap"""

    priority = 0.6
    changefreq = "monthly"

    def items(self):
        # URLs names
        return Product.objects.all()

    def location(self, item):
        """Reverse map location"""
        return reverse(item)


class CategoriesSitemap(sitemaps.Sitemap):
    """Categories sitesmap"""

    priority = 0.6
    changefreq = "monthly"

    def items(self):
        # URLs names
        return Category.objects.all()

    def location(self, item):
        """Reverse map location"""
        return reverse(item)
