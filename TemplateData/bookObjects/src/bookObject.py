from abc import ABC, abstractmethod

class BookObject(ABC):

    dbObject = None
    id:int = None
    name:str = None

    def __init__(self) -> None:
        pass

    @abstractmethod
    def new(self) -> None:
        pass
    
    @abstractmethod
    def open(self, id:int) -> None:
        pass

    @abstractmethod
    def toJSON(self) -> dict:
        return None