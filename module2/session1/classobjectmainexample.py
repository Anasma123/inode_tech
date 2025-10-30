# Simple Example: Bank Account

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.name, "deposited", amount, "Rs. New Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(self.name, "withdrawn", amount, "Rs. Remaining Balance:", self.balance)
        else:
            print("Sorry", self.name + ", insufficient balance!")

            
# Creating two bank accounts
acc1 = BankAccount("Anas", 1000)
acc2 = BankAccount("Fathima", 2000)


# Doing transactions
acc1.deposit(300)
acc1.withdraw(500)

acc2.deposit(800)
acc2.withdraw(2500)
