from django.conf import settings
from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'hyperjob/menu.html')

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'hyperjob/signup.html'

class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'hyperjob/login.html'

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'hyperjob/home.html')
