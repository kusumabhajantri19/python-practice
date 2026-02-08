
#Student class demonstrating encapsulation using private and protected variables

class Student:
    def __init__(self,name,roll_no,age):
        self.name=name
        self._roll_no=roll_no
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>15:
            print("Invalid age given .. Age should be less than 35.")
        else:
            self.__age=age