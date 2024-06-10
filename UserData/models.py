from django.db import models
from freundebuch_testing_2 import db_settings
from TemplateData import models as td

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return(str(self.name))
    
    
class Entry(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    template = models.ForeignKey(td.EntryTemplate, on_delete=models.SET_NULL, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
class Interview(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.SET_NULL, null=True)
    template = models.ForeignKey(td.InterviewTemplate, on_delete=models.SET_NULL, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Answer(models.Model):
    type_choices = db_settings.type_choices
    interview = models.ForeignKey(Interview, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(td.Question, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=100)
    text = models.TextField(max_length=3000)
    image = models.ImageField(upload_to="upload", default="no_image.webp", blank=True)
    #color = answer_color = colorfield.ColorField(default=None, format="rgb", null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)