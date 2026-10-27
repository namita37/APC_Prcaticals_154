from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self, balance=0): self.balance = balance
    @abstractmethod
    def deposit(self, amount): pass
    @abstractmethod
    def withdraw(self, amount): pass
class SavingsAccount(BankAccount):
    def deposit(self, amount): self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance: self.balance -= amount
        else: print("Insufficient balance")
class CurrentAccount(SavingsAccount): pass
a = SavingsAccount(1000); a.deposit(500); a.withdraw(200)
print("Balance:", a.balance)
