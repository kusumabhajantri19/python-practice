

#Animal and Dog classes demonstrating method overriding

class Animal:
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def sound(self):
        print("Bark!")

a = Animal()
a.sound()     # Some generic sound

d = Dog()
d.sound()     # Bark! → overridden
