""" URLs for Gallery """
from django.urls import path

from . import views

urlpatterns = [
    path("", views.list_gallery, name="list_gallery"),
    path("add/<int:product_id>/",
         views.add_galleryitem,
         name="add_galleryitem"),
    path("delete/<int:product_id>/",
         views.delete_galleryitem,
         name="delete_galleryitem"),
]
