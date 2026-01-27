

#Write a Python program to print the first 'n' Fibonacci numbers, where 'n' is input by the user.

num = int(input("enter a number:"))
a = 0
b = 1
for i in range(num):
    print(a,end="")
    temp = a
    a = b
    b = temp+a