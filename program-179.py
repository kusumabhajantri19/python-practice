

#Write a Python program to take 'n' numbers as input from the user and print their sum and average.

num = int(input("enter number:"))
i=0
sum =0
while i<num:
    n = int(input(f"enter number {i+1}: "))
    i=i+1
    sum = sum +n
avg = sum/num
print("sum =",sum)
print("avg =",int(avg))