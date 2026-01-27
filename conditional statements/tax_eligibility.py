

# Determine if a person is eligible to pay tax based on age and income entered by the user.

inc = int(input("Enter a income:"))
age = int(input("Enter your age:"))
if age > 18 and inc >500000:
    print("Eligible for tax")
else:
    print("Not eligible for tax")