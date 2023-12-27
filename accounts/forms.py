from django.contrib.auth.forms import UserCreationForm
from .constants import ACCOUNT_TYPE,GENDER_TYPE
from django import forms
from django.contrib.auth.models import User
# Create your

class UserRegisterForm(UserCreationForm):
    birth_date=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender= forms.CharField(max_length=50, choices=GENDER_TYPE)
    street_address=forms.CharField( max_length=100)
    city=forms.CharField( max_length=50)
    postal_code=forms.IntegerField()
    country=forms.CharField( max_length=50)
    class Meta:
        model= User