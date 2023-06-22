""" Admin for Guestbook module """
from django.contrib import admin
from .models import GuestbookItem


class GuestbookAdmin(admin.ModelAdmin):
    """ Guestbook Admin Model """
    list_display = (
        "name",
        "image",
    )

    ordering = ("name",)


admin.site.register(GuestbookItem, GuestbookAdmin)
