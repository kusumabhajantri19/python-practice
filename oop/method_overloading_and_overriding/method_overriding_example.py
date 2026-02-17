
#Demonstrate Method Overriding using super() in Python

class Father:
    def sleep(self):
        print("Sleeps from 10:00 pm to 5:00 Am")
    def eat(self):
        print("eating")
class Son(Father):
    def sleep(self):
        print("sleep from 8:00 am to 4:00 pm")
        super().sleep()
Ram=Son()
Ram.sleep()