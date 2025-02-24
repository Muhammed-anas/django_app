import django_filters

from .models import Listing

class ListingFilters(django_filters.FilterSet):
    
    class Meta:
        model = Listing
        fields = {'brand':{'exact'}, 'transmission':{'exact'}, 'milege':{'lt'}}
    