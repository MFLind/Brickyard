""" Checkout apps """
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """Config for Checkout"""

    name = "checkout"

    def ready(self):
        """Return ready signal"""
        import checkout.signals
