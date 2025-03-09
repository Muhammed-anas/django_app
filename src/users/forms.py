from django import forms
from django.contrib.auth.models import User
from .models import Profile
from .widgets import CustomPictureImageFieldWidget

class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)
    class Meta:
        model = User
        fields = {'username','first_name','last_name','email'}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.order_fields(['username','first_name','last_name','email'])
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        photo = forms.ImageField(widget=CustomPictureImageFieldWidget)
        model = Profile
        fields = {'photo','bio','phone_number'}