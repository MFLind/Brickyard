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


def p_error_404_view(request):
    return render(request, "home/404.html")


def error_404_view(request, exception):
    return render(request, "home/404.html")


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /accounts/",
        "Disallow: /checkout/",
        "Sitemap: https://brickyard.se/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


@require_GET
def sitemap_xml(request):
    file1 = open("sitemap.xml", "r")
    lines = file1.readlines()
    return HttpResponse("\n".join(lines), content_type="text/plain")
