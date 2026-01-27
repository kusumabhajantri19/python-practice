

#Write a Python program with a function that takes a list as input and returns the list with duplicates removed.

def remove_duplicates(lst):
    return list(set(lst))

nums = [1,2,3,2,1,4,4,5]
print(remove_duplicates(nums))
