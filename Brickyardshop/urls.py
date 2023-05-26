from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("contact", views.contact, name="contact"),
    path("aboutus", views.aboutus, name="aboutus"),
    path("gallery", views.gallery, name="gallery"),
    path("error", views.p_error_404_view, name="error"),
]

handler404 = 'Brickyardshop.views.error_404_view'