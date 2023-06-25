""" Admin for Wishlist module """
from django.contrib import admin
from .models import WishLineItem


class WishListAdmin(admin.ModelAdmin):
    """ Wishlist Admin Model """
    list_display = (
        "name",
        "image",
    )

    ordering = ("name",)


admin.site.register(WishLineItem, guestbook/admin.py)
