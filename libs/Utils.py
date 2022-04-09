from datetime import datetime
from dateutil import relativedelta

# Function calculating interval between two dates
def calc_age(current_date, dob: str) -> int:

    date_of_birth = datetime.strptime(dob, '%Y/%m/%d')
    return relativedelta.relativedelta(current_date, date_of_birth).years
