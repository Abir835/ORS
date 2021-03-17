from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.Front_Page, name='font_page'),
    path('login/', views.LogIn, name='login'),
    path('logout/', views.LogOut, name='logout'),
    path('registration/', views.Registration, name='registration'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('profile/', views.Profile, name='profile'),
    path('status/', views.Status, name='status'),
    path('vacancy/', views.Vacancy, name='vacancy'),
    path('vacancy_details/', views.Vacancy_Details, name='vacancy_details'),
    path('apply/', views.Apply, name='apply'),
    path('Written_exam/', views.Written_Exam, name='written_exam'),

]
