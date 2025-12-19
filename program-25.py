
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

# Check if num1 is the median
if (num2 < num1 < num3) or (num3 < num1 < num2):
    print(num1, "is the median")

# Check if num2 is the median
elif (num1 < num2 < num3) or (num3 < num2 < num1):
    print(num2, "is the median")

# Otherwise num3 is the median
else:
    print(num3, "is the median")