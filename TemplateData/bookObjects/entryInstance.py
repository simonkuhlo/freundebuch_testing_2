from UserData import models as ud
from TemplateData.forms import answerFormSet
from django.forms import BaseModelFormSet
from TemplateData.bookObjects.interviewInstance import InterviewInstance
from TemplateData.bookObjects.entryTemplate import EntryTemplate


class EntryInstance(EntryTemplate):

    entryInstance = None
    interviewInstances:list[InterviewInstance] = None
    template:EntryTemplate = None

    def instanciate(self, author, template) -> any:
        self.template = template
        unsavedEntryObject = ud.Interview.objects.create(
        author = author,
        template = template
        )
        self.entryInstance = unsavedEntryObject.save()
        return self

    def createAnswerForms(self) -> None:
        allIntitialData = []
        for question in self.questions:
            data = {
                'interview' : self.interviewInstance,
                'question' : question,
                'type'  : question.type
            }
            allIntitialData.append(data)
        self.formSet = answerFormSet(initial=allIntitialData)
    
    def toJSON(self) -> dict:
        dict =  super().toJSON()
        dict["formset"] = self.formSet
        return dict