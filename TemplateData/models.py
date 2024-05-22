from django.db import models
from UserData.models import Answer

# Create your models here.

class Question(models.Model):
    name = models.CharField(max_length=100, unique=True)
    default_answertype = models.CharField(max_length=30, choices=Answer.type_choices,unique=True)
    title_de = models.CharField(max_length=100, unique=True)
    desc_de = models.CharField(max_length=1000, unique=True)
    title_en = models.CharField(max_length=100, unique=True)
    desc_en = models.CharField(max_length=1000, unique=True)

class InterviewTemplate(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000, unique=True)
    questions = models.ManyToManyField(Question, through="InterviewQuestions")

class DisplayStyle(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000, unique=True)
    template_path = models.CharField(max_length=1000, unique=True)

class EntryTemplate(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000, unique=True)
    interviews = models.ManyToManyField(InterviewTemplate, through="EntryInterviews")

class EntryInterviews(models.Model):
    entryTemplate = models.ForeignKey(EntryTemplate, on_delete=models.CASCADE)
    index = models.IntegerField()
    interviewTemplate = models.ForeignKey(InterviewTemplate, on_delete=models.CASCADE)

class InterviewQuestions(models.Model):
    interviewTemplate = models.ForeignKey(InterviewTemplate, on_delete=models.CASCADE)
    index = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)