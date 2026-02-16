

#Create a Student class with constructor and display method

class Student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"hi myself {self.name} from student class")
s1=Student("rahul")
print(s1.name)
s1.display()
