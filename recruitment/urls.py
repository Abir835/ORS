from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('', views.Front_Page, name='font_page'),
    path('login/', views.LogIn, name='login'),
    path('logout/', views.LogOut, name='logout'),
    path('registration/', views.Registration, name='registration'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('profile/<int:user_id>', views.Profile, name='profile'),
    path('status/', views.Status, name='status'),
    path('vacancy/', views.Vacancy, name='vacancy'),
    path('vacancy_details/<int:vacancy_id>', views.Vacancy_Details, name='vacancy_details'),
    path('apply/<int:vacancy_id>', views.Apply, name='apply'),
    path('Written_exam/<int:vacancy_id>', views.Written_Exam, name='written_exam'),


    path('application/', views.Application, name='application'),
    path('see_applicant/<int:vacancy_id>', views.See_Applicant, name='see_applicant'),
    path('see_selected_applicant/<int:vacancy_id>', views.See_Selected_Applicant, name='see_selected_applicant'),
    path('applicant_details/<int:apply_id>', views.Applicant_Details, name='applicant_details'),

    path('send-exam-link/<int:vacancy_id>/<int:apply_id>/<int:user_id>/<str:action>', views.SendExamLink.as_view(), name='send_exam_link'),
    path('send-viva-info/<int:vacancy_id>/<int:apply_id>/<int:user_id>', views.SendVivaInfo.as_view(), name='send_viva_info'),

    # Resetting the password
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
         name="password_reset_complete"),

]
