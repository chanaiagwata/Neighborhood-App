from .models import Profile, Post, Neighborhood, Business
from django import forms

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','neighbourhood']
        
class addHoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['admin']
        
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user']