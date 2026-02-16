

# Protected Access Specifier Example

class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self._roll_no=roll_no
    def display(self):
        print(f"hi myself {self.name} with {self._roll_no} from student class")
class Branch(Student):
    pass
def showData():
 b1=Branch("nisha",21)
 print(b1.name)
 # print(b1.roll_no)  //public

showData()
s1=Student("rahul",23)
s1.name="renuka"
s1._roll_no=17
s1.display()