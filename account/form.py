import email
import imp
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import  User

class signupForm(UserCreationForm):
    email=forms.EmailInput()
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password1','password2')

class Edit_Profile(UserChangeForm):
    email=forms.EmailInput()
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username',)
        