
#OOP Example: Class and Instance Variables with Methods in Python

class Instructor:
    followers = 0
    def __init__(self,instructor_name,address):
        self.name=instructor_name
        self.address= address
        # self.followers=0
    def display(self,subject_name):
        print(f"hi,i am {self.name} and i teach {subject_name}")
    def update_followers(self,follower_name):
        self.followers += 1
instructor_1=Instructor("Jenny","Payal")
print(instructor_1.name)
print(instructor_1.address)
instructor_1.display("python")
instructor_1.update_followers("hi")
print(instructor_1.followers)
instructor_2=Instructor("Jenny","Payal")
instructor_2.update_followers("hi")
print(instructor_2.followers)
