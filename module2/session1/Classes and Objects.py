# Program: Create a Simple Bank Account System using Classes and Objects in Python

# -------------------------------
# Class Definition
# -------------------------------
# 'BankAccount' class represents a real-world bank account.
# It allows deposit and withdrawal of money using class methods.

class BankAccount:
    # Constructor: initializes account holder's name and balance
    def __init__(self, name, balance):
        self.name = name         # Account holder's name
        self.balance = balance   # Initial account balance

    # Method to deposit money into the account
    def deposit(self, amount):
        self.balance += amount
        print(self.name, "deposited", amount, "Rs. New Balance:", self.balance)

    # Method to withdraw money from the account
    def withdraw(self, amount):
        # Withdraw only if sufficient balance exists
        if amount <= self.balance:
            self.balance -= amount
            print(self.name, "withdrawn", amount, "Rs. Remaining Balance:", self.balance)
        else:
            print("Sorry", self.name + ", insufficient balance!")


# -------------------------------
# Object Creation
# -------------------------------
# Each account is represented as a separate object.
acc1 = BankAccount("Anas", 1000)       # Account 1 with Rs.1000
acc2 = BankAccount("Fathima", 2000)    # Account 2 with Rs.2000


# -------------------------------
# Performing Transactions
# -------------------------------
# Demonstrating deposit and withdrawal operations.
acc1.deposit(300)      # Anas deposits Rs.300
acc1.withdraw(500)     # Anas withdraws Rs.500

acc2.deposit(800)      # Fathima deposits Rs.800
acc2.withdraw(2500)    # Fathima withdraws Rs.2500
