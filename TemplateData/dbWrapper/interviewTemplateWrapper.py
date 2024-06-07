from TemplateData.dbWrapper.src.dbObjectWrapper import DbObjectWrapper as DbOW
from TemplateData.dbWrapper.questionWrapper import QuestionWrapper

from TemplateData import models as td

from TemplateData import forms

class InterviewTemplateWrapper(DbOW):
    questions:list[QuestionWrapper] = []
    formList = []
    displayStyle:td.DisplayStyle = None

    def __init__(self, dbObject=None, id = None) -> None:
        super().__init__(td.InterviewTemplate, dbObject)
        self.questions:list[QuestionWrapper] = []
        self.formList = []
        self.displayStyle:td.DisplayStyle = None
        self.open(dbObject, id)

    def new(self) -> None:
        return super().new()

    def open(self, object=None, id=None) -> None:
        super().open(object, id)
        self.dbObject:td.InterviewTemplate
        self.displayStyle = self.dbObject.displayStyle
        for object in td.InterviewQuestions.objects.filter(interviewTemplate=self.dbObject):
            self.questions.append(QuestionWrapper(object.question))
    
    def createFormList(self, lang):
        self.formList = []
        for question in self.questions:
            form = forms.answerFormFactory(question.dbObject)
            dict = {
                'question' : question.toJSON(lang),
                'form' : form
            }
            self.formList.append(dict)
        return self.formList
    
    def toJSON(self, lang:str) -> dict:
        dict = super().toJSON()
        dict['name'] = self.dbObject.name
        dict['desc'] = self.dbObject.description
        dict['template'] = self.displayStyle.template_path
        dict['formlist'] = self.createFormList(lang)
        return dict