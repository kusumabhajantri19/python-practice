

#Write a Python program to demonstrate class and object using a Human class with a constructor and a method

class Human:
    def __init__(self,name):
        self.name= name


    def walk(self):
        print(f"{self.name} is walking")

khushi = Human("khushi")
jiya = Human("jiya")
khushi.walk()
jiya.walk()
print(khushi.name)
