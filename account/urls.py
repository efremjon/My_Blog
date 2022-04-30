from django.urls import path
from .views import UserRegistrationView,UpdateProfile,ChagePassword,userprofile
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name="register"),
    path('edit_Profile/',UpdateProfile.as_view(),name="edit_profile"),
    path('<int:pk>/user_profile',userprofile.as_view(),name="user_profile"),
    path('Chage_passwordw/',ChagePassword.as_view(),name='Chage_password'),
]
