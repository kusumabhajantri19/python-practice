


#Person class with optional age

class Person:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

        if age is None:
            print(f"Person name: {name}")
        else:
            print(f"Person name: {name}, age: {age}")


p1 = Person("Alice")      # only name
p2 = Person("Bob", 25)    # name + age