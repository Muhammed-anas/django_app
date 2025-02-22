from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Listing
from .forms import ListingForms, LocationForms

def main_view(request):
    return  render(request, "views/main.html")

@login_required
def home_view(request):
    listings = Listing.objects.all()
    return render(request, "views/home.html", {'listings':listings})

@login_required
def list_view(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        listing_forms = ListingForms()
        location_forms = LocationForms()
    return render (request, 'views/list.html', {'listing_forms':listing_forms},
                   {'location_forms':location_forms})
