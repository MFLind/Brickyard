""" URL for mail site """
from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap, index
from Brickyardshop.sitemap import ProductSitemap, CategoriesSitemap

sitemaps = {
    "products": ProductSitemap,
    "categories": CategoriesSitemap,
}


urlpatterns = [
    path("", views.index, name="home"),
    path("contact", views.contact, name="contact"),
    path("aboutus", views.aboutus, name="aboutus"),
    path("robots.txt", views.robots_txt),
    path("sitemap.xml", views.sitemap_xml),
]

""" urlpatterns += [
    # sitemap.xml index will have all sitemap-......xmls index
    path('sitemap.xml', index, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.index'),

    # sitemap-<section>.xml here <section> will be replaced by the key
    # from sitemaps dict
    path('sitemap-<section>.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]
 """
