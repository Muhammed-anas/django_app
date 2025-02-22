from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Listing

def main_view(request):
    return  render(request, "views/main.html")

@login_required
def home_view(request):
    listings = Listing.objects.all()
    return render(request, "views/home.html", {'listings':listings})
# Create your views here.
