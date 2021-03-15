from django.shortcuts import render


# Create your views here.

def Front_Page(request):
    return render(request, 'front_page.html')


def LogIn(request):
    return render(request, 'login.html')


def Registration(request):
    return render(request, 'registration.html')
