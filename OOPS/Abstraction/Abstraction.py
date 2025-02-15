from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass #Hides the implementation details

    @abstractmethod
    def withdraw(self, amount):
        pass
            
    @abstractmethod
    def balance_enquiry(self):
        pass

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
            return amount
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def balance_enquiry(self):
        print(f"Account Number: {self.account_number}\nBalance: ₹{self.balance}")

# Creating an object of the subclass
account = SavingsAccount("1234567890", 5000)
print(f"Account Number: {account.account_number},  balance: {account.balance}, deposit : {account.deposit(1000)}")
print(f"Account balnce after deposit : {account.balance}")
