from libs.User import User
from libs.Company import Company
import json

def main():
    companies_db = []
    users_db = []
    
    companies_data = json.loads(
        open("./assets/company.json").read())

    for company_data in companies_data: # iterate through raw data companies

        company = Company(
            company_data['id'], 
            company_data['name'],
            company_data['headquarters'], 
            company_data['industry']
        )

        companies_db.append(company) # add company object to companies database


    users_data = json.loads(
        open("./assets/user.json", "r").read())

    for user_data in users_data: # iterate through users in RAW data

        for current_company in companies_db: # iterate through companies in the database

            # check if company exists for user and assign company object
            if current_company.id is not user_data['company_id']: 
                current_company = {}

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

    users_db_json = json.dumps(users_db)
    print(users_db_json)
    

if __name__ == "__main__":
    main()
