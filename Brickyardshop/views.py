""" Views for Brickyardshop """
import logging
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET

logger = logging.getLogger(__name__)


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

    logger.info("error 404: {}", exception)
    return render(request, "home/404.html")


def error_500_view(request):
    """500 - error view"""
    return render(request, "home/500.html")


def error_403_view(request, exception):
    """403 - permission denied view"""
    logger.info("error 403: {}", exception)
    return render(request, "home/403.html")


def error_400_view(request, exception):
    """400 - bad request view"""
    logger.info("error 400: {}", exception)
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
    logger.info("robot_txt reqest: {}", request)
    return HttpResponse("\n".join(lines), content_type="text/plain")


@require_GET
def sitemap_xml(request):
    """sitemap.xml view"""
    lines = ""
    with open("sitemap.xml", "r", encoding='UTF-8') as file1:
        lines = file1.readlines()

    logger.info("sitemap_xml reqest: {}", request)
    return HttpResponse("\n".join(lines), content_type="text/plain")
