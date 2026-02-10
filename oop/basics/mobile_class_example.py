

#Write a Python program to demonstrate class and object using a Mobile class

class Mobile():
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    def say(self):
        print(f"Hi this is {self.brand} of rupees {self.price}")

hi = Mobile("Enova",3000)
hello = Mobile("julia",6700)
hi.say()
hello.say()