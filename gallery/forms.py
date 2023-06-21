""" Forms for Gallery """
from django import forms
from .widgets import CustomClearableFileInput
from .models import GalleryItem


class GalleryForm(forms.ModelForm):
    """ Gallery form """
    class Meta:
        """ Meta class for GalleryForm """
        model = GalleryItem
        fields = "__all__"

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        """ Constructor for gallery form """
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"
