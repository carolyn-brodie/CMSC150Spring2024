from BankAccount import *

class SavingsAccount(BankAccount):

    def __init__(self, owner, acct, balance, rate):
        super().__init__(owner, acct, balance)
        self.interest_rate = rate

    def withdraw(self, amount):
        super().withdraw(amount + 1)

    def pay_interest(self):
        super().deposit(self.interest_rate * self.balance)

    def __str__(self):
        out = super().__str__()
        out += f"\n and Interest Rate: {self.interest_rate}"
        return out

def test():
    print("tester")
    savings1 = SavingsAccount("Suzy", 1234, 100, .1)
    bank1 = BankAccount("Sam", 456)
    print(savings1)
    savings1.pay_interest()
    savings1.deposit(100)
    bank1.deposit(200)
    savings1.withdraw(10)
    bank1.withdraw(10)
    print(savings1)
    print(bank1)

tester()