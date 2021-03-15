from django.db import models


# Create your models here.

class TextBoxDB(models.Model):
    notification = models.CharField(max_length=250)
    writenDate = models.DateTimeField(default=None, null=True)
    vivaDate = models.DateTimeField(default=None, null=True)
    vivaLik = models.CharField(max_length=250)


class VacancyDB(models.Model):
    vId = models.IntegerField(blank=None, null=True)
    vacancy = models.CharField(max_length=100)


class VacancyDetailsDB(models.Model):
    sl = models.IntegerField(blank=None, null=True)
    vacancyNum = models.IntegerField(blank=None, null=True)
    position = models.CharField(max_length=250)
    shortDescription = models.TextField(max_length=500)
    requirement = models.TextField(max_length=1000)
    additionalInformation = models.CharField(max_length=200)
    officeLocation = models.CharField(max_length=100)
    lastDate = models.DateTimeField(default=None, null=True)


class ApplyDB(models.Model):
    applicantID = models.IntegerField(blank=None, null=True)
    name = models.CharField(max_length=25)
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField(max_length=20, default=None, null=True)
    pastExperience = models.CharField(max_length=250, null=True)
    salary = models.CharField(max_length=100)
    university_Name = models.CharField(max_length=100)
    noticePeriod = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    coverLatter = models.FileField(upload_to='CoverLater/')
    Cv = models.FileField(upload_to='Cv/')


class WrittenExamPagedB(models.Model):
    qSl = models.IntegerField(blank=None, null=True)
    label1 = models.CharField(max_length=100)
    label2 = models.TextField(max_length=500)
    label3 = models.TextField(max_length=500)
    label4 = models.TextField(max_length=500)
    label5 = models.TextField(max_length=500)
    label6 = models.TextField(max_length=500)
    label7 = models.TextField(max_length=500)
    label8 = models.TextField(max_length=500)
    label9 = models.TextField(max_length=500)
    label10 = models.TextField(max_length=500)


class WrittenAnsDB(models.Model):
    examId = models.IntegerField(blank=None, null=True)
    definition = models.TextField(max_length=500)
    theory = models.TextField(max_length=500)
    idTest = models.TextField(max_length=500)
    math1 = models.TextField(max_length=500)
    math2 = models.TextField(max_length=500)
    math3 = models.TextField(max_length=500)
    syntax1 = models.TextField(max_length=500)
    syntax2 = models.TextField(max_length=500)
    syntax3 = models.TextField(max_length=500)
    syntax4 = models.TextField(max_length=500)


class DeptDB(models.Model):
    DeptId = models.IntegerField(blank=None, null=True)
    DeptName = models.CharField(max_length=50)


class JobPositionDB(models.Model):
    JobPId = models.IntegerField(blank=None, null=True)
    JobPosition = models.TextField(max_length=500)


class QDetail(models.Model):
    DeptID = models.IntegerField(blank=None, null=True)
    JobPID = models.IntegerField(blank=None, null=True)
    JobPositions = models.TextField(max_length=500)
    startTime = models.DateTimeField(default=None, null=True)
    endTime = models.DateTimeField(default=None, null=True)


class Category(models.Model):
    labelName = models.CharField(max_length=20)

    def __str__(self):
        return self.labelName


class QDetails(models.Model):
    JobPiD = models.IntegerField(blank=None, null=True)
    question = models.TextField(max_length=250)
    categories = models.ManyToManyField('Category',)

    def __str__(self):
        return self.question
