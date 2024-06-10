from django.db import models
from freundebuch_testing_2 import db_settings
# Create your models here.

class Question(models.Model):
    type_choices = db_settings.type_choices
    name = models.CharField(max_length=100, unique=True)
    default_answertype = models.CharField(max_length=30, choices=type_choices)
    title_de = models.CharField(max_length=100)
    desc_de = models.CharField(max_length=1000)
    title_en = models.CharField(max_length=100)
    desc_en = models.CharField(max_length=1000)

    def __str__(self):
        return(str(self.name))

class DisplayStyle(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000)
    template_path = models.CharField(max_length=1000)

    def __str__(self):
        return(str(self.name))
    
class InterviewTemplate(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000)
    questions = models.ManyToManyField(Question, through="InterviewQuestions")
    displayStyle = models.ForeignKey(DisplayStyle, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return(str(self.name))
    
class EntryTemplate(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000)
    interviews = models.ManyToManyField(InterviewTemplate, through="EntryInterviews")

    def __str__(self):
        return(str(self.name))

class EntryInterviews(models.Model):
    entryTemplate = models.ForeignKey(EntryTemplate, on_delete=models.CASCADE)
    index = models.IntegerField()
    interviewTemplate = models.ForeignKey(InterviewTemplate, on_delete=models.CASCADE)

    def __str__(self):
        return(f"{self.entryTemplate} [{self.index}]-> {self.interviewTemplate} ")

class InterviewQuestions(models.Model):
    interviewTemplate = models.ForeignKey(InterviewTemplate, on_delete=models.CASCADE)
    index = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return(f"{self.interviewTemplate} [{self.index}]-> {self.question} ")