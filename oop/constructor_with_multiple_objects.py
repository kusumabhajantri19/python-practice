

#Create a Class with Constructor and Multiple Objects in Python

class Instructor:
    def __init__(self):
        print("Creating a new object")

instructor_1=Instructor()
instructor_1.name="Payal"
instructor_1.address= "Delhi"
print(instructor_1.name)
instructor_2=Instructor()
instructor_2.name="Khushi"
instructor_2.address= "Bengaluru"
print(instructor_2.name)