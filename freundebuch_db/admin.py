from django.contrib import admin
from freundebuch_db import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Question)
admin.site.register(models.Answer)
admin.site.register(models.InterviewTemplate)
admin.site.register(models.InterviewTemplateHasQuestion)
admin.site.register(models.Interview)
admin.site.register(models.InterviewAnswer)
admin.site.register(models.BasicInfo)
admin.site.register(models.Entry)