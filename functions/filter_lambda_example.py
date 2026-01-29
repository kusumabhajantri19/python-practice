#Write a program to filter even numbers from a list using filter() and lambda in Python.

nums = [1,2,3,4]

res = filter(lambda x:x%2==0,nums)

print(list(res))