

# Check if the age entered by the user is valid and determine voting eligibility.

age = int(input("Enter age: "))

if age < 0 or age > 150:
    print("Invalid age")
elif age >= 18:
    print("Eligible for vote")
else:
    print("Not eligible for vote")