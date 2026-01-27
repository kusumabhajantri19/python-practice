

#Write a Python program to calculate the factorial of a given number input by the user.

num = int(input("Enter a number:"))
fact = 1
while num>1:
    fact = fact * num
    num = num-1
print(fact)