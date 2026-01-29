
#Write a function to find the sum of multiple numbers using variable-length arguments.

def add(a):
def add(*a):
    return sum(a)

c = add(1,2,4,6)
print(c)

