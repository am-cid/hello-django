from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ListingForm
from .models import Listing


# Create your views here.
def listing_list(request: HttpRequest) -> HttpResponse:
    listings = Listing.objects.all()
    return render(request, "listings/listing_list.html", {"listings": listings})


def listing_detail(request: HttpRequest, pk: int) -> HttpResponse:
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, "listings/listing_detail.html", {"listing": listing})


def listing_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listing_list")
    else:
        form = ListingForm()
    return render(request, "listings/listing_form.html", {"form": form})


def listing_update(request: HttpRequest, pk: int) -> HttpResponse:
    listing = get_object_or_404(Listing, pk=pk)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect("listing_list")
    else:
        form = ListingForm(instance=listing)
    return render(request, "listings/listing_form.html", {"form": form})


def listing_delete(request: HttpRequest, pk: int) -> HttpResponse:
    listing = get_object_or_404(Listing, pk=pk)
    if request.method == "POST":
        listing.delete()
        return redirect("listing_list")
    return render(request, "listings/listing_confirm_delete.html", {"listing": listing})
