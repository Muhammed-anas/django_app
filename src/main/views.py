from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Listing
from .forms import ListingForms, LocationForms
from .filters import ListingFilters


def main_view(request):
    return render(request, "views/main.html")

@login_required
def home_view(request):
    listings = Listing.objects.all()
    listing_filters = ListingFilters(request.GET, queryset=listings) 
    return render(request, "views/home.html", {'listing_filters':listing_filters})

@login_required
def list_view(request):
    if request.method == 'POST':
        try:
            listing_forms = ListingForms(request.POST, request.FILES)
            location_forms = LocationForms(request.POST)
            if listing_forms.is_valid() and location_forms.is_valid():
                listing = listing_forms.save(commit=False)
                listing_location = location_forms.save()
                listing.seller = request.user.profile
                listing.location = listing_location
                listing.save()
                messages.info(
                    request, f'{listing.brand} {listing.model} posted Successfully')
                return redirect ('home')
            else:
                raise Exception()
        except Exception as e:
            print (e)
            messages.error(
                request, 'Error occured when added the listing'
                )
            
    elif request.method == 'GET':
        listing_forms = ListingForms()
        location_forms = LocationForms()
    return render (request, 'views/list.html', {'listing_forms':listing_forms,
                   'location_forms':location_forms})

def edit_view(request):
    return render (request, 'views/edit.html')
