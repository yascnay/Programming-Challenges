from datetime import datetime, timedelta


def get_date_of_week(year, week_number, day_of_week):
    # Get the first day of the year
    first_day = datetime.strptime(f"01/01/{year}", "%m/%d/%Y").date()

    # Calculate the offset to the first occurrence of the specified day of the week
    days_to_add = (day_of_week - first_day.weekday() + 7) % 7
    fecha_actual= datetime.strptime(f"02/09/{year}", "%m/%d/%Y").date()
    dias_transcurridos = (fecha_actual - first_day).days
    print(dias_transcurridos)

    # Calculate the date of the first occurrence of the specified day of the week in the specified week
    first_occurrence = (first_day + timedelta(days=dias_transcurridos))
    #timedelta(days=days_to_add + 7 * (week_number - 1)))
    print(str(timedelta(days=days_to_add + 7 * (week_number - 1))))


    return first_occurrence

# Example usage


vdate = datetime.today()
day = vdate.day
month = vdate.month
year = vdate.year - 1

actweek = vdate.isocalendar()[1]
dayweek = vdate.isocalendar()[2]


date_of_week = get_date_of_week(year, actweek, dayweek)
print(f"The date of week {actweek} and day {dayweek} in {year} is {date_of_week}")