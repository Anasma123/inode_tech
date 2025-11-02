# ===============================================================
# 💡 Module 2 - Session 7
# Topic: Abstraction + Encapsulation (Bank Account Example)
# ===============================================================

# Import ABC and abstractmethod
# ithu use cheythu abstract class create cheyyunnu
from abc import ABC, abstractmethod


# ---------------------------------------------------------------
# 🔹 Abstract Base Class → Account
# ---------------------------------------------------------------
class Account(ABC):
    def __init__(self, name, balance):
        # private variables (Encapsulation)
        # __name, __balance directly access cheyyan pattilla classinte purath ninn
        self.__name = name
        self.__balance = balance

    # abstract method (Abstraction)
    # every child account type (Savings, Current etc.) must define this
    @abstractmethod
    def calculate_interest(self):
        pass

    # normal concrete method (common for all account types)
    def deposit(self, amount):
        # deposit cheyyunna amount add cheyyunnu balance il
        self.__balance += amount
        print("\nDeposited:", amount)
        print("Updated Balance:", self.__balance)

    # getter method (Encapsulation) — safely access private balance
    def get_balance(self):
        return self.__balance


# ---------------------------------------------------------------
# 🔹 Child Class → SavingsAccount
# ---------------------------------------------------------------
class SavingsAccount(Account):
    # must implement abstract method from Account
    def calculate_interest(self):
        # interest rate fixed as 5%
        interest = self.get_balance() * 0.05
        print("\nInterest (5%):", interest)
        print("Total after interest:", self.get_balance() + interest)


# ---------------------------------------------------------------
# 🔹 User Input Section
# ---------------------------------------------------------------
name = input("Enter Account Holder Name: ")
bal = float(input("Enter Opening Balance: "))
amt = float(input("Enter Deposit Amount: "))

# create savings account object (child class)
acc = SavingsAccount(name, bal)

# deposit money (common method from parent)
acc.deposit(amt)

# calculate interest (implemented in child)
acc.calculate_interest()
