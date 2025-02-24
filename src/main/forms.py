from django import forms

from .models import Listing
from users.models import Location


class ListingForms(forms.ModelForm):
    image = forms.ImageField()
    
    class Meta:
        model = Listing
        fields = {'brand', 'model', 'vin', 'milege', 'color',
                 'description', 'engine', 'transmission'}
        




class LocationForms(forms.ModelForm):
    address1 = forms.CharField(required=True)
    
    
    class Meta:
        model = Location
        fields = {'address1', 'address2', 'city', 'state'}
