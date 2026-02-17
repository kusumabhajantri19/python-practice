
# Basic Method Overriding Example

class Animal:
    def make_sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def make_sound(self):
        print("Dog barks")


a = Animal()
d = Dog()

a.make_sound()
d.make_sound()
