import os

from django import forms
from django.contrib.auth.models import User

from .models import Listing, Profile


class ListingForm(forms.ModelForm):
    picture = forms.ImageField(
        label="Listing Photo", required=False, widget=forms.FileInput
    )
    remove_picture = forms.BooleanField(required=False)

    class Meta:
        model = Listing
        fields = [
            "name",
            "seller_url",
            "description",
            "price",
            "picture",
        ]

    def save(self, commit=True):
        instance = super(ListingForm, self).save(commit=False)
        if self.cleaned_data.get("remove_picture"):
            try:
                os.unlink(instance.picture.path)
            except OSError:
                pass
            instance.picture = None
        if commit:
            instance.save()
        return instance

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full mt-1 border border-gray-300 rounded-md shadow-sm p-2 focus:ring-indigo-500 focus:border-indigo-500',
            'placeholder': 'Enter your password'
        })
    )
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'block w-full mt-1 border border-gray-300 rounded-md shadow-sm p-2 focus:ring-indigo-500 focus:border-indigo-500',
                'placeholder': 'Enter your username'
            }),
        }

class ProfileForm(forms.ModelForm):
    picture = forms.ImageField(
        label="Profile Picture", required=False, widget=forms.FileInput
    )
    remove_picture = forms.BooleanField(required=False)
    cover = forms.ImageField(
        label="Profile Cover", required=False, widget=forms.FileInput
    )
    remove_cover = forms.BooleanField(required=False)

    class Meta:
        model = Profile
        fields = ["bio", "link", "picture", "cover"]
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'block w-full mt-1 border border-gray-300 rounded-md shadow-sm p-2 focus:ring-indigo-500 focus:border-indigo-500',
                'rows': 4,
                'placeholder': 'Write something about yourself...'
            }),
            'link': forms.URLInput(attrs={
                'class': 'block w-full mt-1 border border-gray-300 rounded-md shadow-sm p-2 focus:ring-indigo-500 focus:border-indigo-500',
                'placeholder': 'https://example.com'
            }),
            'picture': forms.FileInput(attrs={
                'class': 'hidden',
                'id': 'id_picture'
            }),
            "cover": forms.FileInput(attrs={"class": "hidden", "id": "id_cover"}),
        }

    def save(self, commit=True):
        instance = super(ProfileForm, self).save(commit=False)
        if self.cleaned_data.get("remove_picture"):
            try:
                os.unlink(instance.picture.path)
            except OSError:
                pass
            instance.picture = None
        if self.cleaned_data.get("remove_cover"):
            try:
                os.unlink(instance.cover.path)
            except OSError:
                pass
            instance.cover = None
        if commit:
            instance.save()
        return instance
