from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Listing, LikedListing
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
                request, 'Error occured when added the listing')
            
    elif request.method == 'GET':
        listing_forms = ListingForms()
        location_forms = LocationForms()
    return render (request, 'views/list.html', {'listing_forms':listing_forms,
                   'location_forms':location_forms})


@login_required
def edit_view(request, id):
    listing = Listing.objects.get(id=id)
    if request.method == 'POST':
        try:
            listing_forms = ListingForms(request.POST, request.FILES, instance=listing)
            location_forms = LocationForms(request.POST, instance=listing.location)
            if listing_forms.is_valid() and location_forms.is_valid():
                listing_forms.save()
                location_forms.save()
                messages.info(
                    request, f'{listing.brand} {listing.model} updated Successfully')
                return redirect ('home')
            else:
                raise Exception()
        except Exception as e:
            print (e)
            messages.error(
                request, 'Error occured when updated the listing')    
    elif request.method == 'GET':
        listing_forms = ListingForms(instance=listing)
        location_forms = LocationForms(instance=listing.location)
    return render (request, 'views/edit.html', {'listing_forms':listing_forms,
                   'location_forms':location_forms})
    
    
@login_required
def details_view(request, id):
    listing = Listing.objects.get(id=id)
    return render (request, 'views/listing.html', {'listing':listing})


@login_required
def delete_post(request, id):
    delete_list = Listing.objects.get(id=id)
    delete_list.delete()
    return redirect('home')


@login_required
def like_list_view(request, id):
    listing = get_object_or_404(Listing, id=id)
    liked_list, created = LikedListing.objects.get_or_create(profile = request.user.profile, listing=listing)
    
    if not created:
        liked_list.delete()
    else:
        liked_list.save()
    
    return JsonResponse({
        'is_liked_by_user': created
    })
    
    