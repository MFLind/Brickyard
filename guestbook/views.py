""" Views for Guestbook """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import GuestbookItem
from .forms import GuestbookForm


def list_guestbook(request):
    """A view that Guestbook"""

    guestbookitems = GuestbookItem.objects.all()

    context = {
        "guestbookitems": guestbookitems,
    }

    return render(request, "guestbook/guestbook.html", context)


@login_required
def add_guestbookitem(request):
    """Add a Guestbook Item to the Guestbook"""
    if not request.user.is_authenticated:
        messages.error(request, "Sorry, only login user can do that.")
        return redirect(reverse("list_guestbook"))

    if request.method == "POST":
        form = GuestbookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added Guestbook Item!")
            return redirect(reverse("list_guestbook"))
        messages.error(
            request,
            "Failed to add Guestbook Item. \
            Please ensure the form is valid.",
        )
    else:
        form = GuestbookForm()

    template = "guestbook/add_guestbookitem.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def delete_guestbookitem(request, guestbookitem_id):
    """Delete a Guestbook Item"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    guestbookitem = get_object_or_404(GuestbookItem, pk=guestbookitem_id)
    guestbookitem.delete()
    messages.success(request, "Guestbook Item deleted!")
    return redirect(reverse("list_guestbook"))
