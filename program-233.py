
#using iterator

class CountDown:
    def __init__(self,start):
        self.start = start

    def __iter__(self):
        return self


    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        num = self.start
        self.start -=1
        return num
cd = CountDown(5)

for i in cd:
    print(i)
