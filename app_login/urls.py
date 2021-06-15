from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

app_name = 'app_login'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('account/register', UserCreationView.as_view(), name="register"),
    path('account/login', LoginView.as_view(), name="login"),
    path('account/logout',
         LogoutView.as_view(template_name='registration/login.html'),
         name="logout"),

]
