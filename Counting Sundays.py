import datetime

def contar():
    domingo = 0
    for year in range(1901, 2001):
        for month in range(1, 13):  
            first_day_of_month = datetime.datetime(year, month, 1)
            if first_day_of_month.weekday() == 6:
                domingo += 1
    return domingo

sundays_on_first_of_month_count = contar()
print("Number of Sundays that fell on the first of the month during the twentieth century:", sundays_on_first_of_month_count)
        