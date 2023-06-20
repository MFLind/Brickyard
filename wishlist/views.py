""" Views for wishlist """
import logging
import hashlib
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from Brickyard import settings

from products.models import Product
from profiles.models import UserProfile
from .models import WishLineItem

logger = logging.getLogger(__name__)


def list_wishlist(request):
    """A view that wishlist"""

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            return redirect(reverse("account_signup"))
    else:
        return redirect(reverse("account_login"))

    wishlist_product_id_list = WishLineItem.objects.filter(user_profile=profile).values_list("product_id", flat=True)
    wish_items = Product.objects.filter(id__in=list(wishlist_product_id_list))

    context = {
        "wishlist_items": wish_items
    }

    return render(request, "wishlist/wishlist.html", context)


def add_wish(request, product_id):
    """Add a product to users wishlist"""

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            return redirect(reverse("account_signup"))
    else:
        return redirect(reverse("account_login"))

    product = get_object_or_404(Product, pk=product_id)
    try:
        wishitem = WishLineItem.objects.get(user_profile=profile, product=product)
    except WishLineItem.DoesNotExist:
        wishitem = None

    if not wishitem:
        wishitem = WishLineItem(user_profile=profile, product=product)
        wishitem.save()

    return redirect(reverse("list_wishlist"))


def delete_wish(request, product_id):
    """Delete a product from the wishlist"""

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            return redirect(reverse("account_signup"))
    else:
        return redirect(reverse("account_login"))

    product = get_object_or_404(Product, pk=product_id)
    try:
        wishitem = WishLineItem.objects.get(user_profile=profile, product=product)
    except WishLineItem.DoesNotExist:
        wishitem = None

    if wishitem:
        wishitem.delete()

    return redirect(reverse("list_wishlist"))
