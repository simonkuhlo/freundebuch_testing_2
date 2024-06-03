class LanguageConverter():
    
    #de is master, must not be None
    de:str = None
    en:str = None

    def __init__(self, de:str=None, en:str=None):
        if de:
            self.de = de
        if en:
            self.en = en

    #add autotranslate if any language is None
    def toDict(self):
        dict = {
            'de' : self.de,
            'en' : self.en
        }
        return dict
    
    def toLanguage(self, lang:str):
        dict = self.toDict()
        #maybe raise error etc.
        if lang in dict.keys():
            return dict[lang]
        else:
            return None