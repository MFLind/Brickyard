""" Views for Gallery """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import GalleryItem
from .forms import GalleryForm


def list_gallery(request):
    """A view that gallery"""

    galleryitems = GalleryItem.objects.all()

    context = {
        "galleryitems": galleryitems,
    }

    return render(request, "gallery/gallery.html", context)


@login_required
def add_galleryitem(request):
    """Add a Gallery Item to the Gallery"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            galleryitem = form.save()
            messages.success(request, "Successfully added Gallery Item!")
            return redirect(reverse("list_gallery"))
        messages.error(
            request,
            "Failed to add Gallery Item. \
            Please ensure the form is valid.",
        )
    else:
        form = GalleryForm()

    template = "gallery/add_galleryitem.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_galleryitem(request, galleryitem_id):
    """Edit a Gallery Item"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    galleryitem = get_object_or_404(GalleryItem, pk=galleryitem_id)
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES, instance=galleryitem)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated gallery item!")
            return redirect(reverse("list_gallery"))
        messages.error(
            request,
            "Failed to update gallery item. \
            Please ensure the form is valid.",
        )
    else:
        form = GalleryForm(instance=galleryitem)
        messages.info(request, f"You are editing {galleryitem.name}")

    template = "gallery/edit_galleryitem.html"
    context = {
        "form": form,
        "galleryitem": galleryitem,
    }

    return render(request, template, context)


@login_required
def delete_galleryitem(request, galleryitem_id):
    """Delete a Gallery Item"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    galleryitem = get_object_or_404(GalleryItem, pk=galleryitem_id)
    galleryitem.delete()
    messages.success(request, "Gallery Item deleted!")
    return redirect(reverse("list_gallery"))
