from libs.User import User
from libs.Company import Company
from libs.Utils import calc_age
from datetime import date
import json, sys

def main():
    companies_db = []
    users_db = []
    date_today = date.today()
    
    try:
        companies_data = json.loads(
            open("./assets/company.json", "r").read())
    except IOError as e:
        print(e)
        print (sys.exc_type)

    for company_data in companies_data: # iterate through companies data

        company = Company(
            company_data['id'], 
            company_data['name'],
            company_data['headquarters'], 
            company_data['industry']
        )

        companies_db.append(company) # add company data to companies database

    try:
        users_data = json.loads(
            open("./assets/user.json", "r").read())
    except IOError as e:
        print(e)
        print (sys.exc_type)


    for user_data in users_data: # iterate through user data

        # filter user based on their date of birth
        if calc_age(date_today, user_data['date_of_birth']) < 30:
            continue

        for current_company in companies_db: # iterate through companies in the database

            # matches user with company and assign company object
            if current_company.id == user_data['company_id']:
                
                user = User(
                    user_data['forename'], 
                    user_data['surname'],
                    user_data['date_of_birth'], 
                    user_data['location'], 
                    # ensure that object is a dictionary
                    # enable JSON serialisation
                    current_company.__dict__ 
                )

            # ensure that object is a dictionary
            # enable json serialisation
            users_db.append(user.__dict__)  

    try:
        users_db_json = json.dumps(users_db)
    except ValueError:
        print('Cannot convert users_db to JSON')
        return

    print(users_db_json)
    

if __name__ == "__main__":
    main()
