class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.name, "deposited", amount, "Rs.")
        print("New Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(self.name, "withdrawn", amount, "Rs.")
            print("Remaining Balance:", self.balance)
        else:
            print("Sorry", self.name + ", insufficient balance!")

    def bankinfo(self, bankname):
        self.bname = bankname
        print("Bank Name:", self.bname)


# ---------- User Input Section ----------
name = input("Enter your Name: ")
balance = float(input("Enter Opening Balance: "))
bankname = input("Enter Bank Name: ")

# Create account object
acc1 = BankAccount(name, balance)

# Display bank info
acc1.bankinfo(bankname)

# Deposit
deposit_amount = float(input("\nEnter amount to Deposit: "))
acc1.deposit(deposit_amount)

# Withdraw
withdraw_amount = float(input("\nEnter amount to Withdraw: "))
acc1.withdraw(withdraw_amount)
