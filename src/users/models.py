from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    bio = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    
def __str__(self):
    return f'{self.user.username}\'s Profile'
