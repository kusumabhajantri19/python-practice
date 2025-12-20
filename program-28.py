
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

sum = num1 + num2

if num1 > 0 and num2 > 0 and sum < 100:
    print("Both are positive and sum is less than 100")
else:
    print("Condition not satisfied")