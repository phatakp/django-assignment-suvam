from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.list import ListView

User = get_user_model()


class HomeView(ListView):
    model = User
    template_name = 'app_login/index.html'
    context_object_name = 'users'


class UserCreationView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('app_login:login')
