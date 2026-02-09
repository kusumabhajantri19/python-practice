

#Method overriding without inheritance

class Human:
    def eat(self):
        print("i can eat ")
    def work(self):
        print("i can work")

class Male:
    def eat(self):
        print("i eat")
    def work(self):
        print("i work")
male_1=Male()
male_1.eat()
