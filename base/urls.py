from django.contrib import admin
from django.urls import path
from base import views
from django.urls import path , include
from django.conf import settings

from account.views import register_view , login_view , logout_view

urlpatterns = [
    path('' , views.homeScreen , name="home"),
    path('login' , login_view , name="login"),
    path('logout' , logout_view , name="logout"),
    path('register' , register_view , name="register"),
]