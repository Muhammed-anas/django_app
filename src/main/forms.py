from django import forms

from .models import Listing



class ListingForms(forms.ModelForm):
    
    
    class Meta:
        model = Listing
        fields = {'brand', 'model', 'vin', 'mileage', 'color',
                 'description', 'engine', 'transmission','image'}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.order_fields(['brand', 'model', 'vin', 'mileage', 'color',
                 'description', 'engine', 'transmission','image'])
        
        
