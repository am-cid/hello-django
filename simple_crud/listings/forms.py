from django import forms
from django.contrib.auth.models import User

from .models import Listing, Profile


class ListingForm(forms.ModelForm):
    picture = forms.ImageField(
        label="Listing Photo", required=False, widget=forms.FileInput
    )
    class Meta:
        model = Listing
        fields = [
            "name",
            "seller_url",
            "description",
            "price",
            "picture",
        ]


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password"]


class ProfileForm(forms.ModelForm):
    picture = forms.ImageField(
        label="Profile Picture", required=False, widget=forms.FileInput
    )
    class Meta:
        model = Profile
        fields = ["bio", "link", "picture"]
