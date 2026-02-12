

#Write a Python program to demonstrate constructor with default arguments using a class

 class Human:
    # def __init__(self,name,age,salary=-1):
    def __init__(self, name="Unknown", age=0, salary=-1):
        print("Consructor is called", name)
        self.name = name
        self.age = age
        self.salary = salary


    def walk(self):
        print(f"{self.name} is walking")

c = Human("jiya",22,5)
d = Human("hi",20)
print(d.salary)
print(c.salary)
c.walk()
d.walk()
papu = Human()
papu.name = "aryan"
papu.walk()