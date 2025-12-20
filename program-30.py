
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day = int(input("Enter a day number (1-7): "))

if 1 <= day <= 7:
    print("Day:", days[day-1])

    if day <= 5:
        print("It's a Weekday")
    else:
        print("It's a Weekend")
else:
    print("Invalid day number")