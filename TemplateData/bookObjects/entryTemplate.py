from TemplateData.bookObjects.src.bookObject import BookObject
from TemplateData import models as td
from TemplateData.bookObjects.interviewTemplate import InterviewTemplate

class EntryTemplate(BookObject):

    description:str = None
    interviewTemplates:list[InterviewTemplate] = []
    
    def new(self) -> None:
        pass

    def open(self, id) -> None:
        entryTemplateObject:td.EntryTemplate = td.EntryTemplate.objects.get(id=id)
        self.id = id
        self.dbObject = entryTemplateObject
        self.name = entryTemplateObject.name
        self.description = entryTemplateObject.description
        for interviewTemplateDBObject in td.InterviewQuestions.objects.filter(interviewTemplate=id):
            self.interviewTemplates.append(InterviewTemplate.open(interviewTemplateDBObject.id))
        return self
    
    def toJSON(self) -> dict:
        dict = {
            'name' : self.name,
            'desc' : self.description,
            'template' : self.displayStyleTemplatePath,
            'interviewTemplates' : [interviewTemplateObject.toJSON for interviewTemplateObject in self.interviewTemplates],
        }
        return dict