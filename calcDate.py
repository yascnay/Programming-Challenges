# Find the date from last year that matches the same week number 
# and day of the week as the current year.
from datetime import datetime
import calendar



vdate = datetime.strptime("03/31/2024", "%m/%d/%Y").date()
day = vdate.day
month = vdate.month
year = vdate.year


actweek = vdate.isocalendar()[1]
dayweek = vdate.isocalendar()[2]

print (
    f"The date of week {actweek} and day {dayweek} in year {year} is: {vdate}")

prevyear= year - 1
lastmonthday= calendar.monthrange(prevyear, month)[1]

for day in range(1, lastmonthday + 1):
    newdate = "{}/{}/{}".format(month, day, prevyear)

    prevdate = datetime.strptime(newdate, "%m/%d/%Y").date()
    prevweek = prevdate.isocalendar()[1]
    prevday = prevdate.isocalendar()[2]
  
    if prevweek == actweek and dayweek == prevday:
        print(
            f"The date of week {actweek} and day {dayweek} in year {prevyear} is: {prevdate}")
        break
    else:

        if day == lastmonthday:
           
            if month== 12:
                nextmonth=1
                prevyear = prevyear + 1
            else:
                nextmonth= month + 1
            lastnexmonth= calendar.monthrange(prevyear, nextmonth)[1]
            for nextday in range(1, lastnexmonth + 1):
                newdate = "{}/{}/{}".format(nextmonth, nextday, prevyear)
                prevdate = datetime.strptime(newdate, "%m/%d/%Y").date()
                prevweek = prevdate.isocalendar()[1]
                prevday = prevdate.isocalendar()[2]
           
                if prevweek == actweek and dayweek == prevday:
                    print(
                        f"The date of week {actweek} and day {dayweek} in year {prevyear} is: {prevdate}")
                    break


