from django.forms import formset_factory
from django import forms
from django.shortcuts import render
from TemplateData import models as td
from UserData import models as ud
from TemplateData.instances import interviewInstance
from TemplateData.dbWrapper import entryTemplateWrapper

class AnswerForm(forms.ModelForm):
    class Meta:
        model = ud.Answer
        exclude = []
        widgets = {'question': forms.HiddenInput()}

def interview_view(request):
    AnswerFormSet = formset_factory(AnswerForm, extra=0)
    if request.method == 'POST':
        formset = AnswerFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                instance = form.save(commit=False)
                instance.save()
    else:
        formset = interviewInstance.create_interviewInstance(
            ud.Entry.objects.get(id=1), 1)
    return render(request, 'interview.html', {'formset': formset})

def test(request, lang):
    entrytemplate = entryTemplateWrapper.EntryTemplateWrapper(id=1).toJSON(lang)
    return render(request, 'interview.html', {'entrytemplate': entrytemplate})