from django import forms

from.models import Listing
from users.models import Location


class ListingForms(forms.ModelForm):
    image = forms.ImageField(required=True)
    
    class Meta:
        model = Listing
        fields = {'brand', 'model', 'vin', 'milege', 'color',
                 'description', 'engine', 'transmission'}
        

class LocationForms(forms.ModelForm):
    pass
    
    class Meta1:
        model = Location
        fields = {'address1, address2', 'city', 'state'}

    