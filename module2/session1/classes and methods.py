# Example 2: Simple Bank Account

# -------------------------------
# Class Definition
# -------------------------------
# This class represents a simple bank account.
# It includes a constructor, and two methods: deposit() and withdraw().
class BankAccount:
    # Constructor method (used to initialize object data)
    def __init__(self, name, balance):
        self.name = name         # Account holder name
        self.balance = balance   # Initial account balance

    # Method to deposit money into the account
    def deposit(self, amount):
        self.balance += amount
        print(self.name, "deposited", amount, "Rs. New Balance:", self.balance)

    # Method to withdraw money from the account
    def withdraw(self, amount):
        # Check if sufficient balance is available
        if amount <= self.balance:
            self.balance -= amount
            print(self.name, "withdrawn", amount, "Rs. Remaining Balance:", self.balance)
        else:
            print("Sorry", self.name + ", insufficient balance!")


# -------------------------------
# Object Creation
# -------------------------------
# Creating two BankAccount objects with name and initial balance
acc1 = BankAccount("Anas", 1000)
acc2 = BankAccount("Fathima", 2000)


# -------------------------------
# Performing Transactions
# -------------------------------
# Deposit and withdraw operations for each account

acc1.deposit(300)     # Anas deposits 300 → New Balance = 1300
acc1.withdraw(500)    # Anas withdraws 500 → Remaining = 800

acc2.deposit(800)     # Fathima deposits 800 → New Balance = 2800
acc2.withdraw(2500)   # Fathima withdraws 2500 → Remaining = 300
