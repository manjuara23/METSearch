from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User 
from .models import Bus,Bus_Route,Bus_Stopage
from django import forms
class UserSignupForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)
    class Meta:
        model = User
        fields=[
            'username',
            'password1',
            'password2',
            'email'
        ]
        
class AddBusStopage(forms.ModelForm):
    class Meta:
        model = Bus_Stopage
        fields=['stopage_name',
                'location']
        
class AddBusRoute(forms.ModelForm):
    class Meta:
        model = Bus_Route
        fields=['bus_stopage',
                'bus']
    
    