

# Print the day of the week based on a number (1-7) entered by the user.

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day = int(input("Enter a day number (1-7): "))

if 1 <= day <= 7:
    print(days[day - 1])
else:
    print("Invalid day number")