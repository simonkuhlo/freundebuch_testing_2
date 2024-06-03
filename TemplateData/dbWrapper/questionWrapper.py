from TemplateData.dbWrapper.src.dbObjectWrapper import DbObjectWrapper as DbOW
from TemplateData.dbWrapper.src.languageConverter import LanguageConverter
from TemplateData import models as td

class QuestionWrapper(DbOW):

    def __init__(self, dbObject:td.Question=None, id:int=None) -> None:
        super().__init__(td.Question, dbObject)
        self.open(dbObject, id)
    
    def new(self) -> None:
        pass

    def open(self, object:td.Question=None, id:int=None) -> None:
        super().open(object, id)
        self.dbObject:td.Question

        dbO = self.dbObject
        self.title = LanguageConverter(dbO.title_de, dbO.title_en)
        self.desc = LanguageConverter(dbO.desc_de, dbO.desc_en)

    def toJSON(self, lang:str) -> dict:
        dict = super().toJSON()
        dict['name'] = self.dbObject.name
        dict['title'] = self.title.toLanguage(lang)
        dict['desc'] = self.desc.toLanguage(lang)
        return dict