import os
from django import forms
from django.contrib.auth.models import User
from .models import Listing, Profile

class ListingForm(forms.ModelForm):
    picture = forms.ImageField(
        label="Listing Photo",
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'block w-full text-sm text-gray-500 border border-gray-300 rounded-lg cursor-pointer focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
        })
    )
    remove_picture = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'h-4 w-4 text-indigo-600 border-gray-300 rounded focus:ring-indigo-500'
        })
    )

    class Meta:
        model = Listing
        fields = ["name", "seller_url", "description", "price", "picture"]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'mt-1 block w-full border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 p-2',
                'placeholder': 'Enter the listing name'
            }),
            'seller_url': forms.URLInput(attrs={
                'class': 'mt-1 block w-full border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 p-2',
                'placeholder': 'https://seller-website.com'
            }),
            'description': forms.Textarea(attrs={
                'class': 'mt-1 block w-full border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 p-2',
                'rows': 4,
                'placeholder': 'Enter a description for your listing'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 p-2',
                'placeholder': 'Enter the price'
            }),
        }

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
            'class': 'mt-1 block w-full border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 p-2',
            'placeholder': 'Enter your password'
        })
    )

    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'mt-1 block w-full border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 p-2',
                'placeholder': 'Enter your username'
            }),
        }


class ProfileForm(forms.ModelForm):
    picture = forms.ImageField(
        label="Profile Picture",
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'block w-full text-sm text-gray-500 border border-gray-300 rounded-lg cursor-pointer focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
        })
    )
    remove_picture = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'h-4 w-4 text-indigo-600 border-gray-300 rounded focus:ring-indigo-500'
        })
    )

    class Meta:
        model = Profile
        fields = ["bio", "link", "picture"]
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'mt-1 block w-full border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 p-2',
                'rows': 4,
                'placeholder': 'Write something about yourself...'
            }),
            'link': forms.URLInput(attrs={
                'class': 'mt-1 block w-full border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 p-2',
                'placeholder': 'https://yourwebsite.com'
            }),
        }

    def save(self, commit=True):
        instance = super(ProfileForm, self).save(commit=False)
        if self.cleaned_data.get("remove_picture"):
            try:
                os.unlink(instance.picture.path)
            except OSError:
                pass
            instance.picture = None
        if commit:
            instance.save()
        return instance
