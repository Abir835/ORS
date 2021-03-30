from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class TextBoxDB(models.Model):
    notification = models.CharField(max_length=250)
    writenDate = models.DateTimeField(default=None, null=True)
    vivaDate = models.DateTimeField(default=None, null=True)
    vivaLik = models.CharField(max_length=250)


class DeptDB(models.Model):
    DeptName = models.CharField(max_length=50)

    def __str__(self):
        return self.DeptName


class VacancyDB(models.Model):
    dept = models.ForeignKey(DeptDB, on_delete=models.SET_NULL, null=True, blank=True)
    vacancy = models.CharField(max_length=100)

    def __str__(self):
        return self.vacancy

    @property
    def get_applications(self):
        return self.applydb_set.all()

    @property
    def get_selected_applicant(self):
        return self.applydb_set.filter(written_link_sent=True)


class JobResponsibilities(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class VacancyDetailsDB(models.Model):
    vacancy = models.OneToOneField(VacancyDB, on_delete=models.SET_NULL, null=True, blank=True)
    CompanyName = models.CharField(max_length=50, null=True)
    vacancyNum = models.IntegerField(blank=None, null=True)
    JobResponsibilities = models.ManyToManyField(JobResponsibilities)
    EmploymentStatus = models.TextField(null=True)
    EducationalRequirements = models.TextField(null=True)
    AdditionalRequirements = models.TextField(null=True)
    JobLocation = models.CharField(max_length=100, null=True)
    salary = models.IntegerField(blank=None, null=True)
    experience = models.CharField(max_length=200, null=True, blank=True)
    lastDate = models.DateTimeField(default=None, null=True)


# Creating VacancyDetailsDB when an User is created.
@receiver(post_save, sender=VacancyDB)
def create_vacancy_details(sender, instance, created, **kwargs):
    if created:
        VacancyDetailsDB.objects.create(vacancy=instance)


class ApplyDB(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    position = models.ForeignKey(VacancyDB, on_delete=models.SET_NULL, null=True, blank=True)
    applicantID = models.IntegerField(blank=None, null=True)
    phoneNumber = models.CharField(max_length=15)
    pastExperience = models.CharField(max_length=250, null=True)
    salary = models.CharField(max_length=100)
    university_Name = models.CharField(max_length=100)
    noticePeriod = models.CharField(max_length=50)
    coverLatter = models.FileField(upload_to='CoverLater/')
    Cv = models.FileField(upload_to='Cv/')

    invitation_sent = models.BooleanField(default=False)
    written_link_sent = models.BooleanField(default=False)
    viva_link_sent = models.BooleanField(default=False)

    apply_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.position.vacancy

    @property
    def status(self):
        if self.written_link_sent is False and self.viva_link_sent is False:
            current_status = "Pending"
        if self.written_link_sent is True and self.viva_link_sent is False:
            current_status = "Selected For Written"
        if self.written_link_sent is True and self.viva_link_sent is True:
            current_status = "Selected For Viva"
        return current_status


class Question(models.Model):
    position = models.ForeignKey(VacancyDB, on_delete=models.SET_NULL, null=True, blank=True)
    questionText = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.questionText)

    @property
    def total_scripts_count(self):
        return self.answer_set.values('user').distinct().count()


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.answer


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    cell = models.CharField(max_length=20, null=True, blank=True)
    university = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return '{}\'s Profile'.format(self.user.username)


# Creating VacancyDetailsDB when an User is created.
@receiver(post_save, sender=User)
def create_user_information(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


class Viva(models.Model):
    link = models.CharField(max_length=300, null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
