""" Views for Brickyardshop """
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from products.models import Category, Product
from django.views.decorators.http import require_GET

# Create your views here.


def index(request):
    """A view to return the index page"""
    return render(request, "home/index.html")


def contact(request):
    """A view to return the contact page"""
    return render(request, "home/contact.html")


def aboutus(request):
    """A view to return the aboutus page"""
    return render(request, "home/aboutus.html")


def links(request):
    """A view to return the links to friends page"""
    return render(request, "home/links.html")


def error_404_view(request, exception):
    """404 - page not found view"""
    return render(request, "home/404.html")


def error_500_view(request):
    """500 - error view"""
    return render(request, "home/500.html")


def error_403_view(request, exception):
    """403 - permission denied view"""
    return render(request, "home/403.html")


def error_400_view(request, exception):
    """400 - bad request view"""
    return render(request, "home/400.html")


@require_GET
def robots_txt(request):
    """robots.txt view"""
    lines = [
        "User-Agent: *",
        "Disallow: /accounts/",
        "Disallow: /checkout/",
        "Sitemap: https://brickyard.herokuapp.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


@require_GET
def sitemap_xml(request):
    """sitemap.xml view"""
    file1 = open("sitemap.xml", "r")
    lines = file1.readlines()
    return HttpResponse("\n".join(lines), content_type="text/plain")
