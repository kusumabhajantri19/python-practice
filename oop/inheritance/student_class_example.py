
# #Q2: Create a class Student with a constructor that sets name and marks. Print the values.

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks


    def hi(self):
        print(f"hi {self.name} has {self.marks} marks")

kk = Student("Khushi", 57)
cat = Student("Hello",56)
kk.hi()
cat.hi()
print(kk.name ,kk.marks)
print(cat.name,cat.marks)