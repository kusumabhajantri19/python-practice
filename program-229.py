#using filter function

nums = [1,2,3,4]

res = filter(lambda x:x%2==0,nums)

print(list(res))