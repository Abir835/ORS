from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.Front_Page),
    path('login/', views.LogIn, name='login'),
    path('registration/', views.Registration, name='registration'),

]
