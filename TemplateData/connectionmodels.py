from django.db import models
from TemplateData import models as Templates

class EntryTemplateInterviewTemplates(models.Model):
    entryTemplate = models.ForeignKey(Templates.EntryTemplate, related_name='connections', on_delete=models.CASCADE)
    interviewTemplate = models.ForeignKey(Templates.InterviewTemplate, related_name='connections', on_delete=models.CASCADE)


class InterviewTemplateQuestions(models.Model):
    pass
