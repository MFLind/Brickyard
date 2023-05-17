from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("webshop", views.webshop, name="webshop"),
    path("contact", views.contact, name="contact"),
    path("aboutus", views.aboutus, name="aboutus"),
    path("gallery", views.gallery, name="gallery"),
]
