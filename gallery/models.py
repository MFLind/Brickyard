""" Models for Gallery """
from django.db import models


class GalleryItem(models.Model):
    """GalleryItem model"""

    name = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """string return of name"""
        return str(self.name)
