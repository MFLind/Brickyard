""" URLs for wishlist """
from django.urls import path

from . import views

urlpatterns = [
    path("", views.list_wishlist, name="list_wishlist"),
    path("add/<int:product_id>/", views.add_wish, name="add_wish"),
    path("delete/<int:product_id>/", views.delete_wish, name="delete_wish"),
]
