
import datetime

print("Hi Khushi!")

# Enter the "current date" (the date you want age calculated from)
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))
current_date = datetime.date(year, month, day)

# Enter Date of Birth
B_year = int(input("Enter birth year: "))
B_month = int(input("Enter birth month: "))
B_day = int(input("Enter birth day: "))
dob = datetime.date(B_year, B_month, B_day)

# Calculate age
age = current_date.year - dob.year
if (current_date.month, current_date.day) < (dob.month, dob.day):
    age -= 1

# Print weekdays and greetings
# print(f"The day of the current date is: {current_date:%A}")
print(f"Today is {current_date:%A} {current_date}. Good evening!")

# Ask height and weight
print("Let’s check your health profile.\nPlease tell me your height (in cm).")
height = int(input("Enter height: "))
print(f"Your height is {height} cm.")

print("Great! Now your weight (in kg)?")
weight = int(input("Enter weight: "))
print(f"Your weight is {weight} kg.")

# Print age
print(f"You are {age} years old.")