from TemplateData import models as td
from UserData import models as ud
from django import forms

class QuestionForm(forms.ModelForm):
    class Meta:
        model = ud.Answer
        exclude = [] # Assuming 'text' is the field for the answer in your Answer model

    def __init__(self, *args, **kwargs):
        self.question = kwargs.pop('question', None)
        super(QuestionForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(QuestionForm, self).save(commit=False)
        instance.question = self.question
        if commit:
            instance.save()
        return instance
td.DisplayStyle.objects.all()