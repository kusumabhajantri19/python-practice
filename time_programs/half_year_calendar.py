

#Print the calendar for the first six months of a given year using the calendar module

import calendar

year = 2025

for month in range(1, 7):
    print(calendar.month(year, month))