""" Forms for Guestbook """
from django import forms
from .widgets import CustomClearableFileInput
from .models import GuestbookItem


class GuestbookForm(forms.ModelForm):
    """Guestbook form"""

    class Meta:
        """Meta class for GuestbookForm"""

        model = GuestbookItem
        fields = ["name", "description", "image"]

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        """Constructor for guestbook form"""
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"
