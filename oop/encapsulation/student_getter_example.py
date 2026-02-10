

#Access private variables using getter method in Python


class Student:
    def __init__(self, name, roll_no, age):
        self.name = name
        self._roll_no = roll_no
        self.__age = age

    def get_age(self):
        return self.__age


s1 = Student("Rahul", 22, 26)
print(s1.get_age())
