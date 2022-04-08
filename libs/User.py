import json 

class User:
    def __init__(self, forename, surname, date_of_birth, location, company) -> None:
        self.forename = forename
        self.surname = surname
        self.full_name = forename + " " + surname # Task 1: Add full_name field
        self.date_of_birth = date_of_birth 
        self.location = location
        self.company = company
