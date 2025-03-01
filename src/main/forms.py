from django import forms

from .models import Listing
from users.models import Location


class ListingForms(forms.ModelForm):
    
    
    class Meta:
        model = Listing
        fields = {'brand', 'model', 'vin', 'mileage', 'color',
                 'description', 'engine', 'transmission','image'}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.order_fields(['brand', 'model', 'vin', 'mileage', 'color',
                 'description', 'engine', 'transmission','image'])
        
        
class LocationForms(forms.ModelForm):
    address1 = forms.CharField(required=True)
    
    
    class Meta:
        model = Location
        fields = {'address1', 'address2', 'city', 'state'}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.order_fields(['address1', 'address2', 'city', 'state'])
