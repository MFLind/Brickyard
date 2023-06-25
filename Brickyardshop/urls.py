""" URL for mail site """
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("contact", views.contact, name="contact"),
    path("aboutus", views.aboutus, name="aboutus"),
    path("links", views.links, name="links"),
    path("robots.txt", views.robots_txt),
    path("sitemap.xml", views.sitemap_xml),
]
