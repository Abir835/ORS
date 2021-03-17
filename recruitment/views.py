from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def Front_Page(request):
    return render(request, 'front_page.html')


def Registration(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created.' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'registration.html', context)


def LogIn(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {}
        return render(request, 'login.html', context)


def LogOut(request):
    logout(request)
    return redirect('font_page')


@login_required(login_url='login')
def Dashboard(request):
    return render(request, 'dashboard.html')


def Profile(request):
    return render(request, 'profile.html')


def Status(request):
    return render(request, 'status.html')


def Vacancy(request):
    return render(request, 'vacancy.html')


def Vacancy_Details(request):
    return render(request, 'vacancy_details.html')


def Apply(request):
    return render(request, 'apply.html')


def Written_Exam(request):
    return render(request, 'written_exam.html')
