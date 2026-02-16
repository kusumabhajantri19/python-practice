

# Private Access Specifier Example


class Student:
    def __init__(self,name,roll_no,age):
        self.name=name
        self._roll_no=roll_no
        self.__age=age
    def __display(self):
        print(f"hi myself {self.name}  {self.__age}with {self._roll_no} from student class")
    def displayprivateData(self):
        self.__display()

class Branch(Student):
    def show(self):
        print(f"my roll_no is {self._roll_no}")
# def showData():
#  b1=Branch("nisha",21)
#  print(b1.name)
#  # print(b1.roll_no)  //public

# showData()
s1=Student("rahul",23,20)
# s1.name="renuka"
# s1._roll_no=17
# s1.display()

print(s1._Student__age)
s1._Student__display()