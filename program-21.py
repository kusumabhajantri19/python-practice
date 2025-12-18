
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = int(input("Enter month number (1-12): "))

if 1 <= month <= 12:
    print(f"Month {month} has {days_in_month[month-1]} days")
else:
    print("Invalid month number")

