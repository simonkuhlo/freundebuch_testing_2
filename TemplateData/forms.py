from TemplateData import models as td
from UserData import models as ud
from django import forms
from django.forms import formset_factory

class AnswerForm(forms.ModelForm):
    class Meta:
        model = ud.Answer
        exclude = []
        widgets = {
            'interview': forms.HiddenInput(),
            'question': forms.HiddenInput(),
            'type': forms.HiddenInput(),
        }

def answerFormFactory(question:td.Question):

    excludeTypes = [value[0] for value in ud.Answer.type_choices]
    if str(question.default_answertype) in excludeTypes:
        excludeTypes.remove(str(question.default_answertype))

    intitialData = {
        'question' : question.id,
        'type'  : question.default_answertype
    }

    class DynamicAnswerForm(AnswerForm):
        class Meta(AnswerForm.Meta):
            exclude = excludeTypes
    form = DynamicAnswerForm(initial=intitialData)
    return form