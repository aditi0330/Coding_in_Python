

from datetime import datetime
from datetime import date

datetime.today()
#datetime.datetime(2020, 3, 19, 14, 38, 52, 133483)

today = datetime.today()


type(today)
#<class 'datetime.datetime'>


todaydate = date.today()

todaydate
#datetime.date(2020, 3, 19)

type(todaydate)
#<class 'datetime.date'>

todaydate.month
#2

todaydate.year
#2020

todaydate.day
#19


christmas = date(2020, 12, 25)
christmas
#datetime.date(2020, 12, 25)

if christmas is not todaydate:
    print("Sorry there are still " + str((christmas - todaydate).days) + " until Christmas!")
else:
    print("Yay it's Christmas!")
    
