

#Person class to check minor or adult

class Person:
    def __init__(self, name, age):
        self.name = name    # store in object
        if age < 18:
            print(f"{name} is a minor")   # age used locally
        else:
            print(f"{name} is an adult")
        self.age = age      # now stored for later use

    def show_info(self):
        print(f"{self.name}, age {self.age}")  # can use self.age


p = Person("Khushi", 15)
p.show_info()