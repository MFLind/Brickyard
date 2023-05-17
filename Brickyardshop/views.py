from django.shortcuts import render

# Create your views here.


def index(request):
    """A view to return the index page"""

    return render(request, "home/index.html")


def webshop(request):
    """A view to return the webshop page"""

    return render(request, "home/webshop.html")


def contact(request):
    """A view to return the contact page"""

    return render(request, "home/contact.html")


def aboutus(request):
    """A view to return the aboutus page"""

    return render(request, "home/aboutus.html")


def gallery(request):
    """A view to return the gallery page"""

    return render(request, "home/gallery.html")
