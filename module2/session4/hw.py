# ============================================================
# Example: Single Inheritance in Python (BankAccount → SavingsAccount)
# Module 2 → Session 4
# ============================================================


# ---------- Parent Class ----------
class BankAccount:
    def __init__(self, account_holder, balance):
        # Constructor to initialize account holder name and balance
        # Ee constructoril account_holderum balanceum store cheyyunnu
        self.account_holder = account_holder
        self.balance = balance

    def show_details(self):
        # Displays account details (holder name and balance)
        # Ee method accountinte details display cheyyunnu
        print("\nAccount Holder:", self.account_holder)
        print("Account Balance:", self.balance)


# ---------- Child Class ----------
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, rate):
        # Calls parent constructor to reuse initialization
        # super() use cheythu parent classinte __init__() call cheyyunnu
        super().__init__(account_holder, balance)

        # Child classil oru puthiya variable rate (interest rate)
        self.rate = rate

    def calculate_interest(self):
        # Formula: Interest = (balance * rate) / 100
        # Ithu oru varshathinu interest calculate cheyyunnu
        interest = (self.balance * self.rate) / 100
        print("Interest after 1 year:", interest)
        return interest


# ---------- User Input ----------
# User ninn account holder name, balance, rate edukkunnu
name = input("Enter Account Holder Name: ")
balance = float(input("Enter Account Balance: "))
rate = float(input("Enter Interest Rate (%): "))


# ---------- Create SavingsAccount Object ----------
# SavingsAccount classinte object undakkunnu
# Ithu BankAccount parent classine inherit cheyyunnath kond
# show_details() method direct use cheyyam
acc = SavingsAccount(name, balance, rate)


# ---------- Display Account Info and Interest ----------
# Parent classil ninnulla method
acc.show_details()

# Child classil define cheytha interest method
acc.calculate_interest()
