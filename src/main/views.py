from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail

from .models import Listing, LikedListing
from .forms import ListingForms
from users.forms import LocationForms
from .filters import ListingFilters


def main_view(request):
    return render(request, "views/main.html")


def home_view(request):
    listings = Listing.objects.all().order_by('-updated_at')
    listing_filters = ListingFilters(request.GET, queryset=listings)
    
    liked_listing_id = []
    if request.user.is_authenticated:
        user_liked_listing = LikedListing.objects.filter(
            profile=request.user.profile).values_list("listing")
        liked_listing_id = [l[0] for l in user_liked_listing]
    return render(request, "views/home.html", {'listing_filters':listing_filters,
                                               'liked_listing_id':liked_listing_id})


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
    liked_list, created = LikedListing.objects.get_or_create(
        profile = request.user.profile, listing=listing)
    if not created:
        liked_list.delete()
    else:
        liked_list.save()
    
    return JsonResponse({
        'is_liked_by_user': created
    })
    
    
@login_required
def inquery_send_mail(request, id):
    listing = get_object_or_404(Listing, id=id)
    try:
        email_subject = f'{request.user.username} is intrested {listing.brand} {listing.model}'
        email_message = f'Hello {listing.seller.user.username}, {request.user.username} is intrested {listing.brand} {listing.model} in listing on Automax'
        send_mail(email_subject, email_message,'AutoLux@gmail.com',
                  [listing.seller.user.email], fail_silently=True)
    except Exception as e:
        print(e)
        return JsonResponse({
            'success':False,
            'info':e
        })
     
@login_required
def users_profile_view(request, id):
    profile_listing = get_object_or_404(Listing, id=id)
    return render (request, "views/profile_page.html",
                   {"profile_listing":profile_listing})
    