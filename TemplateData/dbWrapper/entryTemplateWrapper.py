from TemplateData.dbWrapper.src.dbObjectWrapper import DbObjectWrapper as DbOW
from TemplateData.dbWrapper.interviewTemplateWrapper import InterviewTemplateWrapper

from TemplateData import models as td

class EntryTemplateWrapper(DbOW):
    interviews:list[InterviewTemplateWrapper] = []

    def __init__(self, dbObject=None, id = None) -> None:
        super().__init__(td.EntryTemplate, dbObject)
        self.open(dbObject, id)

    def new(self) -> None:
        return super().new()

    def open(self, object=None, id=None) -> None:
        super().open(object, id)
        self.dbObject:td.EntryTemplate

        for object in td.EntryInterviews.objects.filter(entryTemplate=self.dbObject):
            self.interviews.append(InterviewTemplateWrapper(object.interviewTemplate))
    
    def toJSON(self, lang:str) -> dict:
        print(self.dbObject)
        dict = super().toJSON()
        dict['name'] = self.dbObject.name
        dict['desc'] = self.dbObject.description
        dict['interviews'] = [interview.toJSON(lang) for interview in self.interviews]
        return dict