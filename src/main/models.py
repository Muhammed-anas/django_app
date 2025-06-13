from django.db import models
import uuid
from .consts import CARS_BRANDS, TRANSMISSION_OPTIONS
from .utils import user_listing_path
from cloudinary.models import CloudinaryField
from users.models import Profile, Location

class Listing(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False,
                          default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE) 
    brand = models.CharField(choices=CARS_BRANDS, default=True, max_length=30)
    model = models.CharField(max_length=30)
    vin = models.CharField(max_length=30)
    mileage = models.IntegerField(default=0)
    color =models.CharField(max_length=50)
    description =models.TextField()
    engine = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50, choices=TRANSMISSION_OPTIONS,
                                    default=None)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL,
                                    null=True)
    image = CloudinaryField('image',folder='listings')
    
    def __str__(self):
        return f'{self.seller.user.username}\'s listing - {self.brand} {self.model}'
    
class LikedListing(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    liked_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.listing.brand} {self.listing.model} listing liked by {self.profile.user.username}'