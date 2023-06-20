""" Models for wishlist """
from django.db import models
from products.models import Product
from profiles.models import UserProfile


class WishLineItem(models.Model):
    """ WishLineItem model """
    user_profile = models.ForeignKey(
        UserProfile,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="lineitems",
    )
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )
