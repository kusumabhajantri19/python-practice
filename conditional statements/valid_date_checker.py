

#  Take day and month and check if it forms a valid calendar date (ignoring leap years).

day = int(input("Enter day: "))
month = int(input("Enter month: "))

days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if 1 <= month <= 12 and 1 <= day <= days_in_month[month]:
    print("Valid date")
else:
    print("Invalid date")