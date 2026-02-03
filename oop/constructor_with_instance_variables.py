

#Demonstrate Constructor with Instance Variables in Python OOP

class Instructor:
    def __init__(self,instructor_name,address):
        self.name=instructor_name
        self.address= address
        self.followers=0
instructor_1=Instructor("Jenny","Payal")
print(instructor_1.name)
print(instructor_1.address)
print(instructor_1.followers)
instructor_2=Instructor("Khushi","Priya")
print(instructor_2.name)
print(instructor_2.address)