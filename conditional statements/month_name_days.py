


# Print the name and number of days of a month based on the month number entered by the user.

month_names = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = int(input("Enter month number (1-12): "))

if 1 <= month <= 12:
    print(f"{month_names[month-1]} has {days_in_month[month-1]} days")
else:
    print("Invalid month number")