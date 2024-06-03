from abc import ABC, abstractmethod
from django.db import models

class DbObjectWrapper(ABC):

    model:models.Model = None
    dbObject = None

    def __init__(self, model=None, dbObject=None) -> None:
        self.model = model
        self.open(dbObject)   

    @abstractmethod
    def new(self) -> None:
        pass
    
    def open(self, object=None, id=None) -> None:
        if object:
            if object in self.model.objects.all():
                self.dbObject = object
        elif id:
            self.dbObject = self.model.objects.get(id=id)

    def toJSON(self) -> dict:
        dict = {
            "dbObject" : self.dbObject
        }
        return dict