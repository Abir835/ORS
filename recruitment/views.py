from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import JobPositionDB


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
                email1 = form.cleaned_data.get('email')
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
    data = VacancyDB.objects.all()
    return render(request, 'vacancy.html', {'data': data})


def Vacancy_Details(request):
    return render(request, 'vacancy_details.html')


def Apply(request):
    if request.method == 'POST':
        aid = request.POST.get('aid')
        userName = request.POST.get('userName')
        ephone = request.POST.get('ephone')
        eemail = request.POST.get('eemail')
        pexpreience = request.POST.get('pexpreience')
        esalary = request.POST.get('esalary')
        uname = request.POST.get('uname')
        epriod = request.POST.get('epriod')
        eposition = request.POST.get('eposition')
        ecl = request.FILES.get('ecl')
        ecv = request.FILES.get('ecv')

        myData = ApplyDB(applicantID=aid, name=userName, phoneNumber=ephone, email=eemail, pastExperience=pexpreience,
                         salary=esalary, university_Name=uname, noticePeriod=epriod, position=eposition,
                         coverLatter=ecl, Cv=ecv)
        myData.save()
    return render(request, 'apply.html')


def Written_Exam(request):
    eid = request.POST.get('eid')
    edefinition = request.POST.get('edefinition')
    etheoury = request.POST.get('etheoury')
    eiqtest = request.POST.get('eiqtest')
    emath1 = request.POST.get('emath1')
    emath2 = request.POST.get('emath2')
    emath3 = request.POST.get('emath3')
    esyntax1 = request.POST.get('esyntax1')
    esyntax2 = request.POST.get('esyntax2')
    esyntax3 = request.POST.get('esyntax3')
    esyntax4 = request.POST.get('esyntax4')

    myData = WrittenAnsDB(examId=eid, definition=edefinition, theory=etheoury, iqTest=eiqtest, math1=emath1,
                          math2=emath2, math3=emath3, syntax1=esyntax1, syntax2=esyntax2, syntax3=esyntax3,
                          syntax4=esyntax4)
    myData.save()

    return render(request, 'written_exam.html')
