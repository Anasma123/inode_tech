# =====================================================================
# 🎯 PROJECT: SMARTBIZ MANAGER – Complete Business Management System
# =====================================================================
# Covers all Module 2 Concepts:
# OOP, Inheritance, Polymorphism, Encapsulation, Abstraction,
# File Handling, Regex Validation, Generators, and Search Feature
# =====================================================================

import re                      # For validation
from abc import ABC, abstractmethod  # For abstraction

# ==========================================================
# 🔹 1. Generator for Auto IDs
# ==========================================================
def id_generator(prefix):
    """Auto ID Generator (EMP001, CUST001 etc.)"""
    num = 1
    while True:
        yield f"{prefix}{num:03d}"
        num += 1

emp_gen = id_generator("EMP")
cust_gen = id_generator("CUST")

# ==========================================================
# 🔹 2. Abstract Base Class: Person
# ==========================================================
class Person(ABC):
    def __init__(self, name, email):
        self._name = name       # protected variable
        self._email = email

    @abstractmethod
    def show_details(self):
        pass


# ==========================================================
# 🔹 3. Employee Class (Encapsulation + Polymorphism)
# ==========================================================
class Employee(Person):
    company_name = "SmartBiz Solutions"  # Class variable (shared)

    def __init__(self, name, email, salary):
        super().__init__(name, email)
        self.__salary = salary            # private variable
        self.emp_id = next(emp_gen)       # generator auto id

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("❌ Invalid salary entered")

    def calculate_bonus(self):
        return self.__salary * 0.10

    def show_details(self):
        print(f"\n[Employee ID]: {self.emp_id}")
        print(f"Name: {self._name}")
        print(f"Email: {self._email}")
        print(f"Salary: ₹{self.__salary}")
        print(f"Company: {Employee.company_name}")


# ==========================================================
# 🔹 4. Manager Class (Inheritance + Polymorphism)
# ==========================================================
class Manager(Employee):
    def __init__(self, name, email, salary, dept):
        super().__init__(name, email, salary)
        self.dept = dept

    def calculate_bonus(self):
        return self.get_salary() * 0.20

    def show_details(self):
        super().show_details()
        print(f"Department: {self.dept}")


# ==========================================================
# 🔹 5. Sales Mixin (Multiple Inheritance)
# ==========================================================
class SalesMixin:
    def record_sale(self, amount):
        print(f"✅ Sale of ₹{amount} recorded successfully!")


# ==========================================================
# 🔹 6. Hybrid Inheritance Example
# ==========================================================
class SalesManager(Manager, SalesMixin):
    def __init__(self, name, email, salary, dept, region):
        super().__init__(name, email, salary, dept)
        self.region = region

    def show_details(self):
        super().show_details()
        print(f"Sales Region: {self.region}")


# ==========================================================
# 🔹 7. Customer Class (Another Child of Person)
# ==========================================================
class Customer(Person):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone
        self.cust_id = next(cust_gen)

    def show_details(self):
        print(f"\n[Customer ID]: {self.cust_id}")
        print(f"Name: {self._name}")
        print(f"Email: {self._email}")
        print(f"Phone: {self.phone}")


# ==========================================================
# 🔹 8. File Handling Functions (Add / View / Search / Delete)
# ==========================================================
def save_record(filename, data):
    with open(filename, "a") as f:
        f.write(data + "\n")
    print("✅ Record saved successfully!")

def view_records(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            if not lines:
                print("⚠️ No records found.")
            else:
                print("\n--- Records ---")
                for line in lines:
                    print(line.strip())
    except FileNotFoundError:
        print("❌ File not found.")

def search_record(filename, keyword):
    found = False
    try:
        with open(filename, "r") as f:
            for line in f:
                if keyword.lower() in line.lower():
                    print("✅ Found:", line.strip())
                    found = True
        if not found:
            print("❌ No match found.")
    except FileNotFoundError:
        print("❌ File not found.")

def delete_record(filename, keyword):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
        with open(filename, "w") as f:
            for line in lines:
                if keyword.lower() not in line.lower():
                    f.write(line)
        print("✅ Record deleted (if existed).")
    except FileNotFoundError:
        print("❌ File not found.")


# ==========================================================
# 🔹 9. Validation (Regex)
# ==========================================================
def validate_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

def validate_name(name):
    return re.match(r"^[A-Za-z ]+$", name)

def validate_phone(phone):
    return re.match(r"^\d{10}$", phone)


# ==========================================================
# 🔹 10. Main Menu (User Input)
# ==========================================================
while True:
    print("\n===============================")
    print("    🧾 SMARTBIZ MANAGER SYSTEM")
    print("===============================")
    print("1️⃣ Add Employee")
    print("2️⃣ Add Manager")
    print("3️⃣ Add Sales Manager")
    print("4️⃣ Add Customer")
    print("5️⃣ View Records")
    print("6️⃣ Search Records")
    print("7️⃣ Delete Record")
    print("8️⃣ Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter Employee Name: ")
        if not validate_name(name): print("❌ Invalid name!"); continue
        email = input("Enter Email: ")
        if not validate_email(email): print("❌ Invalid email!"); continue
        salary = float(input("Enter Salary: "))
        emp = Employee(name, email, salary)
        emp.show_details()
        save_record("employees.txt", f"{emp.emp_id},{name},{email},{salary}")

    elif choice == '2':
        name = input("Enter Manager Name: ")
        email = input("Enter Email: ")
        salary = float(input("Enter Salary: "))
        dept = input("Enter Department: ")
        m = Manager(name, email, salary, dept)
        m.show_details()
        save_record("employees.txt", f"{m.emp_id},{name},{email},{salary},{dept}")

    elif choice == '3':
        name = input("Enter Sales Manager Name: ")
        email = input("Enter Email: ")
        salary = float(input("Enter Salary: "))
        dept = input("Enter Department: ")
        region = input("Enter Region: ")
        sm = SalesManager(name, email, salary, dept, region)
        sm.show_details()
        sm.record_sale(50000)
        save_record("employees.txt", f"{sm.emp_id},{name},{email},{salary},{dept},{region}")

    elif choice == '4':
        name = input("Enter Customer Name: ")
        if not validate_name(name): print("❌ Invalid name!"); continue
        email = input("Enter Email: ")
        if not validate_email(email): print("❌ Invalid email!"); continue
        phone = input("Enter Phone Number: ")
        if not validate_phone(phone): print("❌ Invalid phone number!"); continue
        c = Customer(name, email, phone)
        c.show_details()
        save_record("customers.txt", f"{c.cust_id},{name},{email},{phone}")

    elif choice == '5':
        file = input("Enter file name (employees.txt/customers.txt): ")
        view_records(file)

    elif choice == '6':
        file = input("Enter file name: ")
        keyword = input("Enter search keyword: ")
        search_record(file, keyword)

    elif choice == '7':
        file = input("Enter file name: ")
        keyword = input("Enter keyword to delete: ")
        delete_record(file, keyword)

    elif choice == '8':
        print("👋 Thank you for using SmartBiz Manager!")
        break

    else:
        print("❌ Invalid choice. Try again.")
