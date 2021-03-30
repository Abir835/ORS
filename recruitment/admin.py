from django.contrib import admin

# Register your models here.
from .models import TextBoxDB, VacancyDB, VacancyDetailsDB, ApplyDB, DeptDB, \
    JobResponsibilities, UserProfile, Question, Answer, Viva


class TextBoxDBAdmin(admin.ModelAdmin):
    list_display = ('notification', 'writenDate', 'vivaDate', 'vivaLik')


class VacancyDBAdmin(admin.ModelAdmin):
    list_display = ('vacancy',)


class JobResponsibilitiesAdmin(admin.ModelAdmin):
    list_display = ('name',)


class VacancyDetailsDBAdmin(admin.ModelAdmin):
    list_display = (
        'CompanyName', 'vacancyNum',
        'JobLocation', 'salary', 'lastDate')


class ApplyDBAdmin(admin.ModelAdmin):
    list_display = (
        'phoneNumber' , 'pastExperience', 'salary', 'university_Name',
        'noticePeriod', 'position', 'coverLatter', 'Cv', 'apply_date')


class DeptDBAdmin(admin.ModelAdmin):
    list_display = ('DeptName',)


class AnswerDBAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'position', 'question', 'answer', 'time'
    )

    def position(self, obj):
        return obj.question.position.vacancy
    position.admin_order_field = 'question__position'
    position.short_description = 'Position Name'
    list_filter = ['user', 'question__position']


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'position', 'questionText',
    )

    def position(self, obj):
        return obj.position.vacancy
    position.admin_order_field = 'position__vacancy'
    position.short_description = 'Position Name'
    list_filter = ['position__vacancy']


admin.site.register(TextBoxDB, TextBoxDBAdmin)
admin.site.register(VacancyDB, VacancyDBAdmin)
admin.site.register(VacancyDetailsDB, VacancyDetailsDBAdmin)
admin.site.register(ApplyDB, ApplyDBAdmin)
admin.site.register(DeptDB, DeptDBAdmin)
admin.site.register(JobResponsibilities, JobResponsibilitiesAdmin)
admin.site.register(UserProfile)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerDBAdmin)
admin.site.register(Viva)

