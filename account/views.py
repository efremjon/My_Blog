from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class UserRegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_urls = reverse_lazy('login')
# Create your views here.