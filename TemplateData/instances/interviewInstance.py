from django.forms import formset_factory
from django import forms
from TemplateData import models as td
from UserData import models as ud

class AnswerForm(forms.ModelForm):
    class Meta:
        model = ud.Answer
        exclude = []
        widgets = {
                    'interview': forms.HiddenInput(),
                    'question': forms.HiddenInput(),
                    'type': forms.HiddenInput(),
                    }

AnswerFormSet = formset_factory(AnswerForm, extra=0)

def create_interviewInstance(entry, interviewTemplate_id):
    interviewTemplate = td.InterviewTemplate.objects.get(id=interviewTemplate_id)
    interviewInstanceDict = {
        'TemplateName' : interviewTemplate,
        'formset' : None
    }
    unsavedInterviewObject = ud.Interview.objects.create(
        entry = entry, 
        template = td.InterviewTemplate.objects.get(id=interviewTemplate_id)
        )
    interviewObject = unsavedInterviewObject.save()
    allIntitialData = []
    for object in td.InterviewQuestions.objects.filter(interviewTemplate=interviewTemplate_id):
        question = object.question
        data = {
            'interview' : interviewObject,
            'question' : question,
            'type'  : question.default_answertype
        }
        allIntitialData.append(data)
    interviewInstanceDict['formset'] = AnswerFormSet(initial=allIntitialData)
    return interviewInstanceDict