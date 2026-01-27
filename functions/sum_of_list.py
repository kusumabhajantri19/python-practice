
#Write a Python program with a function that takes a list of numbers as input and prints the list and its sum.

nums = [1,2,3,2,1,4,4,5]
def sum(n):
    total = 0
    for n in nums:
        total += n
    print("total nums:",nums)
    print("sum of list:", total)

sum(nums)
