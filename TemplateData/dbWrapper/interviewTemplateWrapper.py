from TemplateData.dbWrapper.src.dbObjectWrapper import DbObjectWrapper as DbOW
from TemplateData.dbWrapper.questionWrapper import QuestionWrapper

from TemplateData import models as td

from TemplateData.forms import answerFormSet

class InterviewTemplateWrapper(DbOW):
    questions:list[QuestionWrapper] = []
    formSet = None
    displayStyle:td.DisplayStyle = None

    def __init__(self, dbObject=None, id = None) -> None:
        super().__init__(td.InterviewTemplate, dbObject)
        self.open(dbObject, id)

    def new(self) -> None:
        return super().new()

    def open(self, object=None, id=None) -> None:
        super().open(object, id)
        self.dbObject:td.InterviewTemplate
        self.displayStyle = self.dbObject.displayStyle
        for object in td.InterviewQuestions.objects.filter(interviewTemplate=self.dbObject):
            self.questions.append(QuestionWrapper(object.question))
    
    def createFormset(self):
        intitialData = []
        for question in self.questions:
            data = {
                'question' : question.dbObject.id,
                'type'  : question.dbObject.default_answertype
            }
            intitialData.append(data)
        self.formSet = answerFormSet(initial=intitialData)
        return self.formSet
    
    def toJSON(self, lang:str) -> dict:
        dict = super().toJSON()
        dict['name'] = self.dbObject.name
        dict['desc'] = self.dbObject.description
        dict['template'] = self.displayStyle.template_path
        dict['formset'] = self.createFormset()
        dict['questions'] = [question.toJSON(lang) for question in self.questions]
        return dict