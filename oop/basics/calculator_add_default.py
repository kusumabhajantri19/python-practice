

#Calculator class with default arguments for addition

class Calculator:
    # Using default arguments
    def add(self, a, b, c=None):
        if c is None:
            return a + b
        else:
            return a + b + c

calc = Calculator()
print(calc.add(2, 3))      # 5
print(calc.add(2, 3, 4))   # 9
