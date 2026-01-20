

#using reduce

from functools import reduce
nums = [1,5,7,8]
def add(a,b):
    return a+b

res = reduce(add,nums)
print(res)
