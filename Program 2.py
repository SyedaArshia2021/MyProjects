from datetime import date
 
def numOfDays(date1, date2):
    return (date2-date1).days
     

date1 = date(2020, 7, 2)
date2 = date(2020, 7, 11)
print(numOfDays(date1, date2), "days")
