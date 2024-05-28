from TemplateData.bookObjects.src.bookObject import BookObject
from TemplateData import models as td
from TemplateData.bookObjects.question import Question

class InterviewTemplate(BookObject):

    description:str = None
    questions:list[Question] = []
    displayStyleDBObject:td.DisplayStyle = None
    displayStyleTemplatePath:str = None
    
    def new(self) -> None:
        pass

    def open(self, id) -> None:
        interviewTemplateObject = td.InterviewTemplate.objects.get(id=id)
        self.id = id
        self.dbObject = interviewTemplateObject
        self.name = interviewTemplateObject.name
        self.description = interviewTemplateObject.description
        self.displayStyleDBObject = td.DisplayStyle.objects.get(interviewTemplateObject.displayStyle)
        self.displayStyleTemplatePath = self.displayStyleDBObject.template_path
        for questionDBObject in td.InterviewQuestions.objects.filter(interviewTemplate=id):
            self.questions.append(Question().open(questionDBObject.id))

    def toJSON(self) -> dict:
        dict = {
            'name' : self.name,
            'desc' : self.description,
            'template' : self.displayStyleTemplatePath,
            'questions' : [questionObject.toJSON for questionObject in self.questions],
        }
        return dict