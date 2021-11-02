from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.views.generic import CreateView
from auth import forms
# Create your views here.

class Login( SuccessMessageMixin,LoginView):
    form_class = forms.LoginAuthenticationForm
    template_name = 'auth/login.html'
    success_url = '/'
    success_message = "Login Successful"

class Signup( SuccessMessageMixin,CreateView):
    model = User
    form_class = forms.SignupForm
    template_name = 'auth/signup.html'
    success_url = '/auth/login/'
    success_message = "Signup Successful. LogIn from here."


class Logout(LogoutView):
    success_url = '/'