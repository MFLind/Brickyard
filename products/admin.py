""" Admin module """
from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """Product Admin Model"""

    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "image",
    )

    ordering = ("sku",)


class CategoryAdmin(admin.ModelAdmin):
    """Category Admin model"""

    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
