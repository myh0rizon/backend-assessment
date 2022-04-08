import json 

class Company:
    def __init__(self, id, name, headquarters, industry) -> None:
        self.id = id
        self.name = name
        self.headquarters = headquarters
        self.industry = industry