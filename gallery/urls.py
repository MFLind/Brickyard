""" URLs for Gallery """
from django.urls import path

from . import views

urlpatterns = [
    path("", views.list_gallery, name="list_gallery"),
    path("add/", views.add_galleryitem, name="add_galleryitem"),
    path(
        "edit/<int:galleryitem_id>/",
        views.edit_galleryitem,
        name="edit_galleryitem",
    ),
    path(
        "delete/<int:galleryitem_id>/",
        views.delete_galleryitem,
        name="delete_galleryitem",
    ),
]
