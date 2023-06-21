""" Admin for Gallery module """
from django.contrib import admin
from .models import GalleryItem


class GalleryAdmin(admin.ModelAdmin):
    """ Product Admin Model """
    list_display = (
        "name",
        "image",
    )

    ordering = ("name",)


admin.site.register(GalleryItem, GalleryAdmin)
