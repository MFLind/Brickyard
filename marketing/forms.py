""" Forms for Marketing """
from django import forms


class EmailForm(forms.Form):
    """Email form"""

    email = forms.EmailField(label="Email", max_length=128)
