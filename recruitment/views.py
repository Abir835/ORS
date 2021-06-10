from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.views.generic.base import View

from ORS.settings import EMAIL_HOST_USER
from .models import *
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail


# Create your views here.

def Front_Page(request):
    return render(request, 'front_page.html')


def Application(request):
    vacancies = VacancyDB.objects.all()

    context = {
        'vacancies': vacancies,
    }

    return render(request, 'applications.html', context)


def See_Applicant(request, vacancy_id):
    vacancy_obj = VacancyDB.objects.get(id=vacancy_id)

    context = {
        'applicants': vacancy_obj.get_applications
    }

    return render(request, 'see_applicant.html', context)


def See_Selected_Applicant(request, vacancy_id):
    vacancy_obj = VacancyDB.objects.get(id=vacancy_id)

    context = {
        'applicants': vacancy_obj.get_selected_applicant
    }
    return render(request, 'see_selected_applicants.html', context)


def Applicant_Details(request, apply_id):
    apply_obj = ApplyDB.objects.get(id=apply_id)

    context = {
        'object': apply_obj
    }

    return render(request, 'applicant_details.html', context)


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

                return redirect('font_page')
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


def Profile(request, user_id):
    user_obj = UserProfile.objects.get(id=user_id)

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        cell = request.POST.get('cell')
        university = request.POST.get('university')

        user_obj.cell = cell
        user_obj.university = university
        user_obj.save()

        user_obj.user.first_name = first_name
        user_obj.user.last_name = last_name
        user_obj.user.save()

        messages.success(request, "Profile Updated Successfully. ")
        return redirect('profile', user_id=user_id)

    context = {
        'object': user_obj
    }

    return render(request, 'profile.html', context)


def Status(request):
    my_applications = ApplyDB.objects.filter(user=request.user)

    context = {
        'applications': my_applications
    }

    return render(request, 'status.html', context)


def Vacancy(request):
    data = VacancyDB.objects.all()
    return render(request, 'vacancy.html', {'data': data})


def Vacancy_Details(request, vacancy_id):
    vacancy_obj = VacancyDetailsDB.objects.get(vacancy__id=vacancy_id)
    responsibilities = vacancy_obj.JobResponsibilities.all()

    context = {
        'object': vacancy_obj,
        'responsibilities': responsibilities,
    }

    return render(request, 'vacancy_details.html', context)


def Apply(request, vacancy_id):
    vacancy_obj = VacancyDB.objects.get(id=vacancy_id)

    if request.method == 'POST':
        ephone = request.POST.get('ephone')
        pexpreience = request.POST.get('pexpreience')
        esalary = request.POST.get('esalary')
        epriod = request.POST.get('epriod')
        uname = request.POST.get('uname')
        ecl = request.FILES.get('ecl')
        ecv = request.FILES.get('ecv')

        myData = ApplyDB(position=vacancy_obj, phoneNumber=ephone, pastExperience=pexpreience,
                         salary=esalary, university_Name=uname, noticePeriod=epriod,
                         coverLatter=ecl, Cv=ecv, user=request.user)
        myData.save()
        messages.success(request, "Thanks for Applying. ")
    return render(request, 'apply.html')


@login_required
def Written_Exam(request, vacancy_id):
    vacancy_obj = VacancyDB.objects.get(id=vacancy_id)

    if request.method == "POST":
        questions_id = request.POST.getlist('question_ids[]')
        answers = request.POST.getlist('answers')

        for i in range(len(questions_id)):
            question_obj = Question.objects.get(id=int(questions_id[i]))
            answer_obj = Answer(user=request.user, question=question_obj, answer=answers[i])
            answer_obj.save()

        messages.success(request, 'Your Script is Submitted Successfully. Result will be sent to you through Email. ')
        return redirect('dashboard')

    context = {
        'object': vacancy_obj,
        'questions': vacancy_obj.question_set.all()
    }

    return render(request, 'written_exam.html', context)


class SendExamLink(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, vacancy_id, apply_id, user_id, action):
        vacancy_obj = VacancyDB.objects.get(id=vacancy_id)
        user_obj = User.objects.get(id=user_id)
        apply_obj = ApplyDB.objects.get(id=apply_id)

        if request.is_secure():
            protocol = 'https://'
        else:
            protocol = 'http://'

        host = request.get_host()
        url = protocol + host + reverse('written_exam', kwargs={'vacancy_id': vacancy_id})

        subject = "Invitation for Written Exam. "

        if action == 'invitation':
            message_text = f"""

                            Hello, {user_obj.username}. Gratings.

                            You are selected for written exam for the post of {vacancy_obj.vacancy}.
                            Your exam will be held on Tomorrow at 10 A.M. 
                            We will send exam link through your email before 5 minutes.
                            Wish you all the best. 

                            Thank You. 

                        """
            apply_obj.invitation_sent = True
            apply_obj.save()
        else:
            message_text = f"""

                    Hello, {user_obj.username}. Gratings.

                    You are selected for written exam for the post of {vacancy_obj.vacancy}.
                    Here is the exam link. Click the link for the Exam. 

                    {url}
                    
                    Note: Exam will be end at 11 A.M. If you submit after 12 P.M., Your answer script will not be accepted.

                    Thank You. 

                """
            apply_obj.written_link_sent = True
            apply_obj.save()

        send_mail(subject, message_text, EMAIL_HOST_USER, [user_obj.email], fail_silently=False)

        if action == 'invitation':
            messages.success(request, 'Invitation Sent Successfully. ')
        else:
            messages.success(request, 'Exam Link Sent Successfully. ')

        return redirect('see_applicant', vacancy_id=vacancy_id)


class SendVivaInfo(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, vacancy_id, apply_id, user_id):
        vacancy_obj = VacancyDB.objects.get(id=int(vacancy_id))
        apply_obj = ApplyDB.objects.get(id=int(apply_id))
        user_obj = User.objects.get(id=int(user_id))

        subject = "Invitation for Viva. "

        viva_obj = Viva.objects.last()
        url = viva_obj.link
        time = viva_obj.time

        message_text = f"""
                    
                    Hello, {user_obj.username}. Gratings.
                    
                    Congratulations. !!! You have done well in your written exam for the post of {vacancy_obj.vacancy}.
                    You are now selected for the next process of our recruitment process: Viva.
                    Here is the viva information. You are requested to join the viva in time. 
                    
                    Link : {url}
                    Time : {time}
                
                    Thank You. 
                    
                """

        send_mail(subject, message_text, EMAIL_HOST_USER, [user_obj.email], fail_silently=False)

        apply_obj.viva_link_sent = True
        apply_obj.save()

        messages.success(request, 'Viva link sent successfully. ')
        return redirect('see_selected_applicant', vacancy_id=vacancy_id)
