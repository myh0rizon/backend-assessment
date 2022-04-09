from libs.Utils import calc_age
from datetime import date 

def test_calc_age():
    date_today = date.today()
    
    # this test will not work in 2023 unless the expected outcome is manually changed
    assert calc_age(date_today, "2001/10/12") == 20