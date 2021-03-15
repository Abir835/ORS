from django.contrib import admin

# Register your models here.
from .models import TextBoxDB, VacancyDB, VacancyDetailsDB, ApplyDB, WrittenExamPagedB, WrittenAnsDB, DeptDB, \
    JobPositionDB, QDetail, Category, QDetails


class TextBoxDBAdmin(admin.ModelAdmin):
    list_display = ('notification', 'writenDate', 'vivaDate', 'vivaLik')


class VacancyDBAdmin(admin.ModelAdmin):
    list_display = ('vId', 'vacancy')


class VacancyDetailsDBAdmin(admin.ModelAdmin):
    list_display = (
        'sl', 'vacancyNum', 'position', 'shortDescription', 'requirement', 'additionalInformation', 'officeLocation',
        'lastDate')


class ApplyDBAdmin(admin.ModelAdmin):
    list_display = (
        'applicantID', 'name', 'phoneNumber', 'email', 'pastExperience', 'salary', 'university_Name',
        'noticePeriod', 'position', 'coverLatter', 'Cv')


class WrittenExamPagedBAdmin(admin.ModelAdmin):
    list_display = (
        'qSl', 'label1', 'label2', 'label3', 'label4', 'label5', 'label6',
        'label7', 'label8', 'label9', 'label10')


class WrittenAnsDBAdmin(admin.ModelAdmin):
    list_display = (
        'examId', 'definition', 'theory', 'idTest', 'math1', 'math2', 'math3',
        'syntax1', 'syntax2', 'syntax3', 'syntax4')


class DeptDBAdmin(admin.ModelAdmin):
    list_display = ('DeptId', 'DeptName')


class JobPositionDBAdmin(admin.ModelAdmin):
    list_display = ('JobPId', 'JobPosition')


class QDetailAdmin(admin.ModelAdmin):
    list_display = ('DeptID', 'JobPID', 'JobPositions', 'startTime', 'endTime')


class QDetailsAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(TextBoxDB, TextBoxDBAdmin)
admin.site.register(VacancyDB, VacancyDBAdmin)
admin.site.register(VacancyDetailsDB, VacancyDetailsDBAdmin)
admin.site.register(ApplyDB, ApplyDBAdmin)
admin.site.register(WrittenExamPagedB, WrittenExamPagedBAdmin)
admin.site.register(WrittenAnsDB, WrittenAnsDBAdmin)
admin.site.register(DeptDB, DeptDBAdmin)
admin.site.register(JobPositionDB, JobPositionDBAdmin)
admin.site.register(QDetail, QDetailAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(QDetails, QDetailsAdmin)
