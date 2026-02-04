
# Create a class Car with attributes brand, price and print them using an object.

class Car:         #Class created
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price    #Attributes created


    def walk(self):
            print(f"Hi this is {self.brand} of rupees {self.price}")  #methods created

ok = Car("Mercede", 100000)  #Objects created
hl = Car("Hello", 60000)
ok.walk()   #Calling objects
hl.walk()
print(ok.brand)  #Printing just value of ok brand value that is 100000