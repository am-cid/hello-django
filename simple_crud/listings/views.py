from django.shortcuts import get_object_or_404, render


# Create your views here.
def listing_list(request: HttpRequest) -> HttpResponse:
    listings = Listing.objects.all()
    return render(request, "listings/listing_list.html", {"listings": listings})


def listing_detail(request: HttpRequest, pk: int) -> HttpResponse:
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, "listings/listing_detail.html", {"listing": listing})
