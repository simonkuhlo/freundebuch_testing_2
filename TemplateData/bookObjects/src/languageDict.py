class LanguageDict():
    #de is master, must not be None
    de:str = None
    en:str = None

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