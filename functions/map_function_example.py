
#Using map function

nums = [1,2,3,4]

def double(x):
    return x+2
res = map(double,nums)

print(list(res))