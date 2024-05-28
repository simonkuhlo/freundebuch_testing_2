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

answerFormSet = formset_factory(AnswerForm, extra=0)