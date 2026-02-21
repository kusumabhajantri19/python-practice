

#Operator Overloading of Greater Than (>) using gt Method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return self.age > other.age


p1 = Person("John", 16)
p2 = Person("Ji", 45)

if p1 > p2:
    print(f"{p1.name} will pay bill")
else:
    print(f"{p2.name} will pay bill")