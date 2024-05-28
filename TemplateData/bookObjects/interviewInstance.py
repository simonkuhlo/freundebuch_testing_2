from UserData import models as ud
from TemplateData.forms import answerFormSet
from django.forms import BaseModelFormSet
from TemplateData.bookObjects.interviewTemplate import InterviewTemplate


class InterviewInstance(InterviewTemplate):

    formSet:BaseModelFormSet = None
    interviewInstance:ud.Interview = None

    def instanciate(self, entry) -> any:
        unsavedInterviewObject = ud.Interview.objects.create(
        entry = entry, 
        template = self.dbObject
        )
        self.interviewInstance = unsavedInterviewObject.save()
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