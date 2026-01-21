#using generator

def simple_gen(x):
    for i in range(x):
        yield i

gen = simple_gen(5)
# print(next(gen))
# print(next(gen))
# print(next(gen))
c=0
for i in gen:
    if c>2:
        break
    print(i)
    c+=1
