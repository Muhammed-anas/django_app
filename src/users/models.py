from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from localflavor.us.models import USStateField

from .utils import user_directory_path
# Create your models here.

class Location(models.Model):
    address1 = models.CharField(max_length=200,blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = USStateField(default='NY')
    
    def __str__(self):
        return f'Location {self.id}'
  
    

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = CloudinaryField('image',null=True)
    bio = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    location = models.OneToOneField(Location,on_delete=models.SET_NULL,
                                    null=True)

    
    def __str__(self):
        return f'{self.user.username}\'s Profile'
