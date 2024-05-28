from TemplateData.bookObjects.src.bookObject import BookObject
from TemplateData.bookObjects.src.languageDict import LanguageDict
from TemplateData import models as td

class Question(BookObject):

    type:str = None
    title:LanguageDict = LanguageDict()
    description:LanguageDict = LanguageDict()
    
    def new(self) -> None:
        pass

    def open(self, id) -> None:
        questionObject = td.Question.objects.get(id=id)
        self.id = id
        self.dbObject = questionObject
        self.name = questionObject.name
        self.type = questionObject.default_answertype
        self.title.de = questionObject.title_de
        self.title.en = questionObject.title_en
        self.description.de = questionObject.desc_de
        self.description.en = questionObject.desc_en
        return self

    def toJSON(self, lang:str) -> dict:
        dict = {
            'name' : self.name,
            'title' : self.title.toLanguage(lang),
            'desc' : self.description.toLanguage(lang)
        }
        return dict