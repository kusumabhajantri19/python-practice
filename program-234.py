
# Generators

def simple_gen():
    yield 1
    yield 2
    yield 3

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

for i in gen:
    print(i)