
#Write a Python program with a function that takes a number as input and prints whether it is even or odd.

def string(n):
    if n % 2==0:
        print("even")
    else:
        print("odd")
num = int(input("Enter a number:"))
string(num)