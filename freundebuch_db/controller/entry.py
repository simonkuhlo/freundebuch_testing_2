from freundebuch_db import models

class Entry():
    user:models.User
    basic_info:models.BasicInfo
    interview:models.Interview
    
    def __init__(self, id=None):
        if id:
            pass
    
    