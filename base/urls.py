from django.contrib import admin
from django.urls import path
from base import views
from django.urls import path , include
from django.conf import settings

from account.views import register_view , login_view , logout_view , account_search_view 

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('' , views.homeScreen , name="home"),
    path('login' , login_view , name="login"),
    path('logout' , logout_view , name="logout"),
    path('register' , register_view , name="register"),
    path('search' , account_search_view , name="search"),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
     name='password_reset_complete'),
]