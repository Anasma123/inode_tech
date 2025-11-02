# Program: Create a Bank Account System using User Input, Classes, and Methods in Python

# -------------------------------
# Class Definition
# -------------------------------
# The 'BankAccount' class represents a customer’s bank account.
# It includes methods for deposit, withdrawal, and displaying bank details.

class BankAccount:
    # Constructor to initialize account holder name and balance
    def __init__(self, name, balance):
        self.name = name          # Account holder's name
        self.balance = balance    # Initial account balance

    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print(self.name, "deposited", amount, "Rs.")
        print("New Balance:", self.balance)

    # Method to withdraw money (with balance check)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(self.name, "withdrawn", amount, "Rs.")
            print("Remaining Balance:", self.balance)
        else:
            print("Sorry", self.name + ", insufficient balance!")

    # Method to display bank information
    def bankinfo(self, bankname):
        self.bname = bankname
        print("Bank Name:", self.bname)


# -------------------------------
# User Input Section
# -------------------------------
# Taking account details from user
name = input("Enter your Name: ")
balance = float(input("Enter Opening Balance: "))
bankname = input("Enter Bank Name: ")

# Create an object (account) using user input
acc1 = BankAccount(name, balance)

# Display bank information
acc1.bankinfo(bankname)

# -------------------------------
# Transaction Section
# -------------------------------
# Perform deposit
deposit_amount = float(input("\nEnter amount to Deposit: "))
acc1.deposit(deposit_amount)

# Perform withdrawal
withdraw_amount = float(input("\nEnter amount to Withdraw: "))
acc1.withdraw(withdraw_amount)
