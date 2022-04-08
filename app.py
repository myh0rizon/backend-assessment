from libs.User import User
from libs.Company import Company
import json

def main():
    companies_db = []
    users_db = []
    
    companies_data = json.loads(open("./assets/company.json").read())

    for company_data in companies_data:
        company = Company(
            company_data['id'], 
            company_data['name'],
            company_data['headquarters'], 
            company_data['industry']
        )
        companies_db.append(company)

    users_data = json.loads(open("./assets/user.json", "r").read())

    for user_data in users_data:
        user = User(
            user_data['forename'], 
            user_data['surname'],
            user_data['date_of_birth'], 
            user_data['location'], 
            user_data['company_id']
        )
        users_db.append(user)
        print(user.full_name)

    print(users_db)
if __name__ == "__main__":
    main()
