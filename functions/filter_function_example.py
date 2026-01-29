#Write a program to filter even numbers from a list using filter() in Python.

nums = [1,2,3,4]
def is_even(x):
    return x%2==0
res = filter(is_even,nums)

print(list(res))