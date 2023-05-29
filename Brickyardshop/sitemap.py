from django.contrib import sitemaps
from django.urls import reverse
from products.models import Product, Category


class ProductSitemap(sitemaps.Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        # URLs names
        return Product.objects.all()

    def location(self, item):
        return reverse(item)


class CategoriesSitemap(sitemaps.Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        # URLs names
        return Category.objects.all()

    def location(self, item):
        return reverse(item)
