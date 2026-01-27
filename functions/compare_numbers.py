

#Write a Python program with a function that takes two numbers as input and prints which one is greater or smaller.

def number(a,b):
    if a > b:
        print(f"{a}  is greater than number {b}")
    else:
        print(f"number {a} is less than number {b}")
# number(3,2)
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
number(num1,num2)