from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import ProfileModel,SignUpModel


class SignUpForm(forms.ModelForm):
    class Meta:
        model =SignUpModel
        fields = ['username', 'email', 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['profile_picture']
 