""" Admin for Wishlist module """
from django.contrib import admin
from .models import WishLineItem


class WishListAdmin(admin.ModelAdmin):
    """ Wishlist Admin Model """
    list_display = (
        "user_profile",
        "product",
    )

    ordering = ("user_profile",)


admin.site.register(WishLineItem, WishListAdmin)
