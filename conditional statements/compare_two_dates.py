
#Take two dates (day and month) and determine which one comes first in the
# calendar.


day1 = int(input("Enter first date day: "))
month1 = int(input("Enter first date month: "))

day2 = int(input("Enter second date day: "))
month2 = int(input("Enter second date month: "))

if month1 < month2:
    print("First date comes first")
elif month1 > month2:
    print("Second date comes first")
else:  # months are equal
    if day1 < day2:
        print("First date comes first")
    elif day1 > day2:
        print("Second date comes first")
    else:
        print("Both dates are the same")