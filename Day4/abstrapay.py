from abc import ABC,abstractmethod
class payment(ABC):
    def pay(self):
        pass
class cashpayment(payment):
    def pay(self,amount):
        print(f"paid ₹{amount} in cash")
class cardpayment(payment):
    def pay(self,amount):
        print(f"paid ₹{amount} using credit/debit card")
class upipayment(payment):
    def pay(self,amount):
        print(f"paid ₹{amount} using upi")
l1=[cashpayment(),cardpayment(),upipayment()]
for i in l1:
    i.pay(1000)