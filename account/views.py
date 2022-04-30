from pyexpat import model
from django.shortcuts import render,reverse
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from .form import signupForm,Edit_Profile
from django.views.generic import DetailView
from myblog.models import profile
from django.shortcuts import get_object_or_404, render


class UserRegistrationView(CreateView):
    form_class = signupForm
    template_name = 'registration/register.html'
    success_urls = reverse_lazy('login')
# Create your views here.
class UpdateProfile(UpdateView):
    form_class = Edit_Profile
    template_name = 'registration/edit_profile.html'
    success_urls = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    def get_success_url(self):
        return reverse('home')

class ChagePassword(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/chage_password'
    def get_success_url(self):
        return reverse('home')
class userprofile(DetailView):
    model = profile
    template_name = 'registration/profile_page.html'
    def get_context_data(self, *args, **kwargs):
        context=super(userprofile,self).get_context_data(*args, **kwargs)
        user_profile=get_object_or_404(profile,id=self.kwargs['pk'])
        context["user_profile"]=user_profile
        
        return context