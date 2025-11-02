# ==========================================================
# 💡 Module 2 – Session 6
# Topic: Encapsulation + Abstraction
# Example: Bank Account Management System
# ==========================================================

from abc import ABC, abstractmethod

# ----------------------------------------------------------
# 🏦 Abstract Base Class (Abstraction Part)
# ----------------------------------------------------------
# Abstraction → hide the complex logic inside the class and expose only necessary methods.
# Parent class defines structure (rules) but not the full implementation.
class Account(ABC):

    def __init__(self, name, acc_no, balance):
        # private variables (Encapsulation)
        self.__name = name
        self.__acc_no = acc_no
        self.__balance = balance
        self._bank_name = "SBI Bank"     # protected variable (subclass can access)

    # ---------- Getter methods ----------
    def get_name(self):
        return self.__name

    def get_acc_no(self):
        return self.__acc_no

    def get_balance(self):
        return self.__balance

    # ---------- Setter method ----------
    def set_balance(self, new_balance):
        # validation: negative balance not allowed
        if new_balance >= 0:
            self.__balance = new_balance
            print("✅ Balance updated successfully:", self.__balance)
        else:
            print("❌ Invalid balance amount!")

    # ---------- Deposit ----------
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited {amount}. New Balance:", self.__balance)
        else:
            print("❌ Deposit amount must be positive!")

    # ---------- Withdraw ----------
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"✅ Withdrawn {amount}. Remaining Balance:", self.__balance)
        else:
            print("❌ Insufficient funds or invalid amount!")

    # ---------- Abstract Method ----------
    @abstractmethod
    def calculate_interest(self):
        # child classes must implement this
        pass

    # ---------- Display Details ----------
    def show_details(self):
        print("\n========= ACCOUNT DETAILS =========")
        print("Bank Name:", self._bank_name)
        print("Account Holder:", self.__name)
        print("Account Number:", self.__acc_no)
        print("Current Balance:", self.__balance)
        print("===================================")


# ----------------------------------------------------------
# 💰 Child Class 1: Savings Account
# ----------------------------------------------------------
class SavingsAccount(Account):
    def __init__(self, name, acc_no, balance, rate):
        super().__init__(name, acc_no, balance)
        self.__rate = rate  # private variable (encapsulated)

    # implement abstract method
    def calculate_interest(self):
        interest = self.get_balance() * (self.__rate / 100)
        print(f"💵 Interest @ {self.__rate}% =", round(interest, 2))
        total = self.get_balance() + interest
        print("💰 Total after Interest:", round(total, 2))


# ----------------------------------------------------------
# 🏢 Child Class 2: Current Account
# ----------------------------------------------------------
class CurrentAccount(Account):
    def __init__(self, name, acc_no, balance, limit):
        super().__init__(name, acc_no, balance)
        self.__limit = limit  # private variable for overdraft limit

    # implement abstract method
    def calculate_interest(self):
        # current account has no interest, show limit instead
        print("⚙️ Current accounts have no interest.")
        print("Overdraft Limit:", self.__limit)


# ----------------------------------------------------------
# ✨ Main Program with User Input
# ----------------------------------------------------------
print("========= BANK ACCOUNT SYSTEM =========")
name = input("Enter Account Holder Name: ")
acc_no = input("Enter Account Number: ")
balance = float(input("Enter Initial Balance: "))

print("\nChoose Account Type:")
print("1. Savings Account")
print("2. Current Account")
choice = int(input("Enter choice (1 or 2): "))

if choice == 1:
    rate = float(input("Enter Interest Rate (%): "))
    acc = SavingsAccount(name, acc_no, balance, rate)
elif choice == 2:
    limit = float(input("Enter Overdraft Limit: "))
    acc = CurrentAccount(name, acc_no, balance, limit)
else:
    print("Invalid choice! Exiting...")
    exit()

# ---------- Perform Operations ----------
acc.show_details()

dep = float(input("\nEnter amount to deposit: "))
acc.deposit(dep)

wd = float(input("Enter amount to withdraw: "))
acc.withdraw(wd)

acc.calculate_interest()

new_bal = float(input("\nEnter new balance (for setter test): "))
acc.set_balance(new_bal)

acc.show_details()
