from abc import ABC,abstractmethod
class balance(ABC):
    @abstractmethod
    def get_balance():
        pass
class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance=self.__balance+amount
    def withdraw(self,amount):
        if(self.__balance-amount<0):
            print("Insufficient")
            return
        self.__balance=self.__balance-amount
    def get_balance(self):
        return self.__balance
n=int(input("Enter intial amount:"))
b=Bank(n)
while True:
    print("deposit 1:\n withdraw 2: \n show balance 3: \nexit:")
    k=int(input())
    if k==1:
        b.deposit(int(input("amount to deposit:")))
    elif k==2:
        b.withdraw(int(input("amount to withdraw:")))
    elif k==3:
        print("showing amount:")
        print(b.get_balance())
    else:
        break