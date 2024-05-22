from django.contrib import admin

# Register your models here.
from TemplateData import models
# Register your models here.
admin.site.register(models.DisplayStyle)
admin.site.register(models.EntryInterviews)
admin.site.register(models.EntryTemplate)
admin.site.register(models.InterviewQuestions)
admin.site.register(models.InterviewTemplate)
admin.site.register(models.Question)