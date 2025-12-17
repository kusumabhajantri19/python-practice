
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both are even")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Both are odd")
else:
    print("One is even and one is odd")