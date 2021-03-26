from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

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
    path('application/', views.Application, name='application'),
    path('see_applicant/', views.See_Applicant, name='see_applicant'),
    path('applicant_details/', views.Applicant_Details, name='applicant_details'),

]
