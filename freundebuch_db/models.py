from django.db import models

# Create your models here.
class Question(models.Model):
    name = models.CharField(max_length=100, unique=True)
    title_de = models.CharField(max_length=300, unique=True)
    desc_de = models.CharField(max_length=1000, unique=True)
    title_en = models.CharField(max_length=300, unique=True)
    desc_en = models.CharField(max_length=1000, unique=True)
    
    def __str__(self):
        return(str(self.name))


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=100, unique=True)
    
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    image = models.CharField(max_length=300, unique=True)
    text = models.CharField(max_length=3000, unique=True)
    #color = models.CharField(max_length=300, unique=True)


class InterviewTemplate(models.Model):
    name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=1000, unique=True)
    
    def __str__(self):
        return(str(self.name))


class InterviewTemplateHasQuestion(models.Model):
    template = models.ForeignKey(InterviewTemplate, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)




class InterviewAnswer(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.SET_NULL, null=True)


class BasicInfo(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    entry_image = models.ManyToManyField(Answer, related_name='entry_image')
    date_of_birth = models.ManyToManyField(Answer, related_name='date_of_birth')
    country_of_origin = models.ManyToManyField(Answer, related_name='country_of_origin')
    first_encounter = models.ManyToManyField(Answer, related_name='first_encounter')
    about_me = models.ManyToManyField(Answer, related_name='about_me')



