

#Create a Class with a Method to Print Numbers from 1 to 4

class Hello:
    def hi(self):
        for i in range(1,5):  #No Constructor,No attributes,although runs
            print(i)            #if you call methods then you need objects
hh = Hello()
hh.hi()