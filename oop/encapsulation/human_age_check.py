

#Create a Human class that prints if a person is a minor or adult based on age

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        if age < 18:
            print(f"{name} is a minor")
        else:
            print(f"{name} is an adult")
hh = Human("Khushi", 15)
jj = Human("Ji", 20)