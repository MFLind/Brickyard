from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from products.models import Category, Product

# Create your views here.


def index(request):
    """A view to return the index page"""

    return render(request, "home/index.html")


def webshop(request):
    """A view to return the webshop page"""

    context = {
        "categories": Category.objects.filter().order_by("friendly_name"),
        "products": Product.objects.filter(category=0).order_by("name"),
    }
    return render(request, "home/webshop.html", context)


def contact(request):
    """A view to return the contact page"""

    return render(request, "home/contact.html")


def aboutus(request):
    """A view to return the aboutus page"""

    return render(request, "home/aboutus.html")


def gallery(request):
    """A view to return the gallery page"""

    return render(request, "home/gallery.html")
