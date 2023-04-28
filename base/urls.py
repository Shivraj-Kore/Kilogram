from django.contrib import admin
from django.urls import path
from base import views
from django.urls import path , include
from django.conf import settings

urlpatterns = [
    path('' , views.homeScreen , name="home"),
    path('register' , views.registerView , name="register"),
]