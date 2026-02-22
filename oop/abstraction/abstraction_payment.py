

#Demonstrate abstraction for payment methods

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class PaypalPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Paypal")

c = CreditCardPayment()
p = PaypalPayment()

c.pay(100)
p.pay(200)