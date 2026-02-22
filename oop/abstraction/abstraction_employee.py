

#Demonstrate abstraction using employee salary example

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Developer(Employee):
    def __init__(self, base):
        self.base = base

    def calculate_salary(self):
        return self.base + 1000  # bonus

dev = Developer(5000)
print("Developer salary:", dev.calculate_salary())