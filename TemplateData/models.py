from django.db import models
from TemplateData import connectionmodels
from UserData import Answer
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
    questions = models.ManyToManyField(Question)
    def get_questions():
        pass

class DisplayStyle(models.Model):
    name = models.CharField(max_length=100, unique=True)


class EntryTemplate(models.Model):
    name = models.CharField(max_length=100, unique=True)
    interviews = models.ManyToManyField(InterviewTemplate)