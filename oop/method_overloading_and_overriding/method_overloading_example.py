

#Demonstrate Method Overloading using args in Python

class Demo:
    def add(self,*args):
        total=0
        for i in args:
            total=total+i
        return total
d=Demo()
print(d.add(1,2))
print(d.add(3,5,7))
print(d.add(8,7,6,5,3))