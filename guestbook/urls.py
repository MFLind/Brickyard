""" URLs for Guestbook """
from django.urls import path

from . import views

urlpatterns = [
     path("", views.list_guestbook, name="list_guestbook"),
     path("add/", views.add_guestbookitem, name="add_guestbookitem"),
     path("delete/<int:guestbookitem_id>/", views.delete_guestbookitem, name="delete_guestbookitem"),

]
