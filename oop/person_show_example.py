

#Person class with optional age and display method

class Person:
    def __init__(self, name, age=None):
        """
        Constructor with optional age parameter.
        If age is not provided, only name is stored.
        """
        self.name = name
        self.age = age

    def show(self):
        """
        Display the details of the person.
        """
        if self.age is None:
            print(f"Person name: {self.name}")
        else:
            print(f"Person name: {self.name}, age: {self.age}")


# Creating objects
p1 = Person("Alice")        # Only name
p2 = Person("Bob", 25)      # Name + age

# Calling show method
p1.show()
p2.show()
