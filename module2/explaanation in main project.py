# =====================================================================
# 🎯 PROJECT: SMARTBIZ MANAGER – Complete Business Management System
# =====================================================================
# Covers all Module 2 Concepts:
# OOP, Inheritance, Polymorphism, Encapsulation, Abstraction,
# File Handling, Regex Validation, Generators, and Search Feature
# =====================================================================

import re                      # For validation
# import = Python keyword to include external modules
# re = Regular Expressions module for pattern matching
# This module helps validate email, phone numbers, names etc.
# re module import cheyyunnath string patterns check cheyyan - email, phone number okke validate cheyyan

from abc import ABC, abstractmethod  # For abstraction
# from = import specific parts from a module
# abc = Abstract Base Classes module  
# ABC = Abstract Base Class - cannot create objects directly
# abstractmethod = decorator to define abstract methods
# abc module ninnu ABC and abstractmethod import cheyyunnu - abstract classes create cheyyan

# ==========================================================
# 🔹 1. Generator for Auto IDs
# ==========================================================
def id_generator(prefix):
    """Auto ID Generator (EMP001, CUST001 etc.)"""
    # def = define a new function
    # id_generator = function name
    # prefix = parameter - what we pass to function
    # This function will generate automatic IDs like EMP001, CUST001
    # Itha function automatic aayi IDs generate cheyyum - EMP001, CUST001 pole
    
    num = 1
    # num = variable name
    # 1 = starting value
    # Initialize counter variable starting from 1
    # Counter variable 1 ninnu thudangunnu
    
    while True:
        # while = loop that continues until condition is False  
        # True = always true condition
        # This creates infinite loop that never stops automatically
        # Itha infinite loop aaanu - automatically stop aavilla
        
        yield f"{prefix}{num:03d}"
        # yield = generator keyword - returns value but remembers position
        # f"" = f-string for formatting
        # prefix = parameter value (EMP, CUST etc.)
        # num:03d = format number as 3 digits with leading zeros
        # This creates IDs like EMP001, EMP002, CUST001 etc.
        # Itha IDs generate cheyyum - EMP001, EMP002, CUST001 ennokke
        
        num += 1
        # num += 1 = increment num by 1 (same as num = num + 1)
        # Increase counter by 1 for next ID
        # Counter ne 1 koodi increase cheyyunnu next ID ku

# Generator objects create cheyyunnu
emp_gen = id_generator("EMP")
# emp_gen = variable name
# id_generator("EMP") = call function with "EMP" as prefix
# Creates generator for employee IDs starting with EMP
# Itha employee IDs generate cheyyan ulla generator undaakunnu - EMP prefix vechu

cust_gen = id_generator("CUST")
# cust_gen = variable name  
# id_generator("CUST") = call function with "CUST" as prefix
# Creates generator for customer IDs starting with CUST
# Itha customer IDs generate cheyyan ulla generator undaakunnu - CUST prefix vechu

# ==========================================================
# 🔹 2. Abstract Base Class: Person
# ==========================================================
class Person(ABC):
    # class = keyword to define a class
    # Person = class name
    # (ABC) = inherits from Abstract Base Class
    # This is abstract class - cannot create objects directly
    # Itha abstract class aaanu - direct aayittu objects create cheyyaan pattilla
    
    def __init__(self, name, email):
        # def = define method
        # __init__ = constructor method - automatically called when object created
        # self = reference to current object instance
        # name, email = parameters
        # Constructor method - initializes object with name and email
        # Itha constructor method - object create cheyyumpol automatically call aavum
        
        self._name = name       # protected variable
        # self._name = protected attribute (single underscore)
        # name = parameter value assigned to attribute
        # Protected variable - can be accessed in child classes
        # Itha protected variable - child classes il access cheyyaam
        
        self._email = email
        # self._email = protected attribute  
        # email = parameter value assigned to attribute
        # Protected variable for email address
        # Itha email address store cheyyan ulla protected variable

    @abstractmethod
    def show_details(self):
        # @abstractmethod = decorator making this method abstract
        # def show_details = method definition
        # Abstract method - must be implemented in child classes
        # Itha abstract method - child classes il implement cheyyanam
        pass
        # pass = placeholder - no implementation in abstract class
        # Just indicates method exists but has no code here
        # Itha just indicate cheyyunnu method undennu - actual code child class il varum

# ==========================================================
# 🔹 3. Employee Class (Encapsulation + Polymorphism)
# ==========================================================
class Employee(Person):
    # class Employee = define Employee class
    # (Person) = inherits from Person class
    # Employee class extends Person class with additional features
    # Employee class Person class ninnu inherit cheyyunnu - extra features add cheyyum
    
    company_name = "SmartBiz Solutions"  # Class variable (shared)
    # company_name = class variable (not instance variable)
    # "SmartBiz Solutions" = value assigned
    # Class variable - shared by all objects of this class
    # Itha class variable - ella Employee objects um same value share cheyyum

    def __init__(self, name, email, salary):
        # Constructor for Employee class
        # name, email, salary = parameters
        # Initializes Employee object with name, email and salary
        # Itha Employee object initialize cheyyunnu - name, email, salary vechu
        
        super().__init__(name, email)
        # super() = refers to parent class (Person)
        # __init__ = call parent constructor
        # Calls Person class constructor to initialize name and email
        # Parent class (Person) inte constructor call cheyyunnu - name, email initialize cheyyan
        
        self.__salary = salary            # private variable
        # self.__salary = private attribute (double underscore)
        # salary = parameter value assigned
        # Private variable - cannot access directly from outside class
        # Itha private variable - class outside ninnu direct aayittu access cheyyaan pattilla
        
        self.emp_id = next(emp_gen)       # generator auto id
        # self.emp_id = employee ID attribute
        # next(emp_gen) = get next value from emp_gen generator
        # Automatically generates employee ID like EMP001
        # Automatic aayi employee ID generate cheyyunnu - EMP001, EMP002 ennokke

    def get_salary(self):
        # Getter method for salary - encapsulation
        # Returns the private salary value
        # Private salary value access cheyyan ulla getter method
        return self.__salary
        # return = returns value from function
        # self.__salary = private salary attribute
        # Returns the salary value
        # Salary value return cheyyunnu

    def set_salary(self, new_salary):
        # Setter method for salary - encapsulation with validation
        # new_salary = parameter - new salary value to set
        # Updates salary with validation check
        # Salary update cheyyan ulla setter method - validation um undu
        if new_salary > 0:
            # if = conditional statement
            # new_salary > 0 = check if new salary is positive
            # Validates that salary is greater than 0
            # Salary 0 inekkal kooduthal aano enn check cheyyunnu
            self.__salary = new_salary
            # self.__salary = private attribute
            # new_salary = parameter value
            # Updates the salary if validation passes
            # Validation pass aayal salary update cheyyunnu
        else:
            # else = executed when if condition is false
            # What happens when salary is not positive
            # Salary positive alla enkil ee code execute aavum
            print("❌ Invalid salary entered")
            # print = output to console
            # "❌ Invalid salary entered" = error message
            # Shows error message for invalid salary
            # Invalid salary enna error message show cheyyunnu

    def calculate_bonus(self):
        # Method to calculate bonus - polymorphism example
        # Calculates 10% of salary as bonus
        # Bonus calculate cheyyan ulla method - salary le 10% bonus aayi
        return self.__salary * 0.10
        # return = returns calculated value
        # self.__salary * 0.10 = 10% of salary
        # Returns bonus amount (10% of salary)
        # Salary le 10% bonus aayi return cheyyunnu

    def show_details(self):
        # Implementation of abstract method - polymorphism
        # Shows all employee details
        # Abstract method implement cheyyunnu - employee details show cheyyan
        print(f"\n[Employee ID]: {self.emp_id}")
        # print = output to console
        # f"" = formatted string
        # \n = new line
        # Shows employee ID with label
        # Employee ID label um koodi show cheyyunnu
        print(f"Name: {self._name}")
        # Shows employee name
        # Employee name show cheyyunnu
        print(f"Email: {self._email}")
        # Shows employee email
        # Employee email show cheyyunnu
        print(f"Salary: ₹{self.__salary}")
        # Shows employee salary with ₹ symbol
        # Employee salary rupee symbol um koodi show cheyyunnu
        print(f"Company: {Employee.company_name}")
        # Shows company name from class variable
        # Class variable il ninnu company name show cheyyunnu

# ==========================================================
# 🔹 4. Manager Class (Inheritance + Polymorphism)
# ==========================================================
class Manager(Employee):
    # class Manager = define Manager class
    # (Employee) = inherits from Employee class
    # Manager class extends Employee with department feature
    # Manager class Employee class ninnu inherit cheyyunnu - department feature add cheyyum
    
    def __init__(self, name, email, salary, dept):
        # Constructor for Manager class
        # name, email, salary, dept = parameters
        # Initializes Manager with additional department information
        # Manager object initialize cheyyunnu - department details um koodi
        super().__init__(name, email, salary)
        # super() = parent class (Employee)
        # __init__ = call parent constructor
        # Calls Employee constructor to initialize name, email, salary
        # Parent class (Employee) inte constructor call cheyyunnu
        self.dept = dept
        # self.dept = department attribute
        # dept = parameter value assigned
        # Stores department information for manager
        # Manager inte department details store cheyyunnu

    def calculate_bonus(self):
        # Method overriding - polymorphism
        # Managers get 20% bonus instead of 10%
        # Bonus calculation method override cheyyunnu - managers ku 20% bonus
        return self.get_salary() * 0.20
        # return = returns calculated value
        # self.get_salary() = calls getter method for salary
        # * 0.20 = 20% of salary
        # Returns 20% of salary as bonus for managers
        # Manager salary le 20% bonus aayi return cheyyunnu

    def show_details(self):
        # Method overriding - extends parent method
        # Shows manager details including department
        # Parent method extend cheyyunnu - department details um koodi show cheyyan
        super().show_details()
        # super() = parent class (Employee)
        # .show_details() = call parent's show_details method
        # Calls Employee's show_details to display basic info
        # Parent class inte show_details method call cheyyunnu - basic details show cheyyan
        print(f"Department: {self.dept}")
        # print = output to console
        # Shows department information
        # Department details show cheyyunnu

# ==========================================================
# 🔹 5. Sales Mixin (Multiple Inheritance)
# ==========================================================
class SalesMixin:
    # class SalesMixin = mixin class for sales functionality
    # Mixin = class that provides additional functionality to other classes
    # Sales related features add cheyyan ulla mixin class
    
    def record_sale(self, amount):
        # Method to record sales
        # amount = parameter - sale amount
        # Records a sale with given amount
        # Sale record cheyyan ulla method
        print(f"✅ Sale of ₹{amount} recorded successfully!")
        # print = output to console
        # f"" = formatted string with amount
        # ✅ = success emoji
        # Shows success message with sale amount
        # Sale amount um koodi success message show cheyyunnu

# ==========================================================
# 🔹 6. Hybrid Inheritance Example
# ==========================================================
class SalesManager(Manager, SalesMixin):
    # class SalesManager = defines SalesManager class
    # (Manager, SalesMixin) = multiple inheritance from Manager and SalesMixin
    # Hybrid inheritance - inherits from both Manager and SalesMixin
    # Multiple inheritance - Manager um SalesMixin um ninnu inherit cheyyunnu
    
    def __init__(self, name, email, salary, dept, region):
        # Constructor for SalesManager
        # name, email, salary, dept, region = parameters
        # Initializes SalesManager with all details including region
        # SalesManager object initialize cheyyunnu - region details um koodi
        super().__init__(name, email, salary, dept)
        # super() = refers to first parent class (Manager)
        # __init__ = call parent constructor
        # Calls Manager constructor to initialize name, email, salary, dept
        # Parent class (Manager) inte constructor call cheyyunnu
        self.region = region
        # self.region = region attribute
        # region = parameter value assigned
        # Stores sales region information
        # Sales region details store cheyyunnu

    def show_details(self):
        # Method overriding - shows sales manager details
        # Extends manager details with region information
        # Manager details extend cheyyunnu - region details um koodi show cheyyan
        super().show_details()
        # super() = parent class (Manager)
        # .show_details() = call parent's show_details method
        # Calls Manager's show_details to display basic info
        # Parent class inte show_details method call cheyyunnu
        print(f"Sales Region: {self.region}")
        # print = output to console
        # Shows sales region information
        # Sales region details show cheyyunnu

# ==========================================================
# 🔹 7. Customer Class (Another Child of Person)
# ==========================================================
class Customer(Person):
    # class Customer = defines Customer class
    # (Person) = inherits from Person class
    # Customer class extends Person with phone number feature
    # Customer class Person class ninnu inherit cheyyunnu - phone number feature add cheyyum
    
    def __init__(self, name, email, phone):
        # Constructor for Customer class
        # name, email, phone = parameters
        # Initializes Customer with name, email and phone number
        # Customer object initialize cheyyunnu - name, email, phone number vechu
        super().__init__(name, email)
        # super() = parent class (Person)
        # __init__ = call parent constructor
        # Calls Person constructor to initialize name and email
        # Parent class (Person) inte constructor call cheyyunnu
        self.phone = phone
        # self.phone = phone attribute
        # phone = parameter value assigned
        # Stores customer phone number
        # Customer phone number store cheyyunnu
        self.cust_id = next(cust_gen)
        # self.cust_id = customer ID attribute
        # next(cust_gen) = get next value from cust_gen generator
        # Automatically generates customer ID like CUST001
        # Automatic aayi customer ID generate cheyyunnu - CUST001, CUST002 ennokke

    def show_details(self):
        # Implementation of abstract method
        # Shows all customer details
        # Abstract method implement cheyyunnu - customer details show cheyyan
        print(f"\n[Customer ID]: {self.cust_id}")
        # print = output to console
        # Shows customer ID with label
        # Customer ID label um koodi show cheyyunnu
        print(f"Name: {self._name}")
        # Shows customer name
        # Customer name show cheyyunnu
        print(f"Email: {self._email}")
        # Shows customer email
        # Customer email show cheyyunnu
        print(f"Phone: {self.phone}")
        # Shows customer phone number
        # Customer phone number show cheyyunnu

# ==========================================================
# 🔹 8. File Handling Functions (Add / View / Search / Delete)
# ==========================================================
def save_record(filename, data):
    # def = define function
    # save_record = function name
    # filename, data = parameters
    # Function to save records to file
    # File il records save cheyyan ulla function
    
    with open(filename, "a") as f:
        # with open() = safe way to open files (automatically closes)
        # filename = name of file to open
        # "a" = append mode - adds to end of file without deleting existing content
        # f = file object variable
        # Opens file in append mode for writing
        # File append mode il open cheyyunnu - existing content delete aakilla
        
        f.write(data + "\n")
        # f.write() = write data to file
        # data = parameter value to write
        # + "\n" = adds new line after data
        # Writes data to file with new line
        # Data file il write cheyyunnu - new line um koodi
    
    print("✅ Record saved successfully!")
    # print = output to console
    # Shows success message after saving
    # Save aayathinu shesham success message show cheyyunnu

def view_records(filename):
    # Function to view all records from file
    # File il ninnu ella records um kandu pidikkan ulla function
    
    try:
        # try = attempt to run code that might cause errors
        # Tries to open and read the file
        # Error varumennu thonnunna code try block il idunnu
        
        with open(filename, "r") as f:
            # with open() = safe file opening
            # filename = name of file to open
            # "r" = read mode - only for reading, not writing
            # f = file object variable
            # Opens file in read mode
            # File read mode il open cheyyunnu - read cheyyan matram
            
            lines = f.readlines()
            # f.readlines() = reads all lines from file into list
            # lines = variable storing all lines as list
            # Reads all lines from file and stores in list
            # File il ninnu ella lines um read cheythu list aakunnu
            
            if not lines:
                # if not lines = check if lines list is empty
                # Checks if file has no records
                # File il records illanno enn check cheyyunnu
                print("⚠️ No records found.")
                # print = output to console
                # Shows message when no records found
                # Records illenkil message show cheyyunnu
            else:
                # else = executed when if condition is false (lines has data)
                # When records are found in file
                # Records undel ee code execute aavum
                print("\n--- Records ---")
                # print = output to console
                # Shows header for records
                # Records in header show cheyyunnu
                for line in lines:
                    # for loop = iterates through each line in lines list
                    # line = current line in loop
                    # Loops through each record in file
                    # Ella lines ilum loop cheyyunnu
                    print(line.strip())
                    # print = output to console
                    # line.strip() = removes extra spaces and newlines from line
                    # Shows each record without extra spaces
                    # Extra spaces remove cheythu each record show cheyyunnu
                    
    except FileNotFoundError:
        # except = handles specific error (FileNotFoundError)
        # FileNotFoundError = occurs when file doesn't exist
        # Handles case when file is not found
        # File kandu pidikkatha pol varunna error handle cheyyunnu
        print("❌ File not found.")
        # print = output to console
        # Shows error message when file doesn't exist
        # File illenkil error message show cheyyunnu

def search_record(filename, keyword):
    # Function to search for records containing keyword
    # File il ninnu specific keyword ulla records kandu pidikkan ulla function
    
    found = False
    # found = boolean variable to track if record found
    # False = initial value (not found yet)
    # Variable to track whether any record was found
    # Records kandu pidichittundo enn track cheyyan ulla variable
    
    try:
        # try = attempt code that might cause errors
        # Tries to search in file
        # Error varumennu thonnunna code try block il idunnu
        
        with open(filename, "r") as f:
            # with open() = safe file opening
            # filename = name of file to open
            # "r" = read mode
            # f = file object variable
            # Opens file for reading
            # File read mode il open cheyyunnu
            
            for line in f:
                # for loop = iterates through each line in file
                # line = current line being checked
                # Loops through each record in file
                # File le ella lines ilum loop cheyyunnu
                
                if keyword.lower() in line.lower():
                    # if = conditional check
                    # keyword.lower() = converts keyword to lowercase
                    # in = membership operator (checks if keyword exists in line)
                    # line.lower() = converts line to lowercase
                    # Case-insensitive search for keyword in line
                    # Case insensitive aayi keyword line il undo enn check cheyyunnu
                    
                    print("✅ Found:", line.strip())
                    # print = output to console
                    # ✅ = success emoji
                    # line.strip() = removes extra spaces
                    # Shows found record with success indicator
                    # Kandu pidicha record success message um koodi show cheyyunnu
                    
                    found = True
                    # found = boolean variable
                    # True = sets to true since record was found
                    # Marks that at least one record was found
                    # Oru record kandu pidichath kond found variable true aakunnu
            
            if not found:
                # if not found = check if no records were found
                # Executes when found is still False (no matches)
                # Oru record um kandilla enkil ee code execute aavum
                print("❌ No match found.")
                # print = output to console
                # ❌ = error emoji
                # Shows message when no matches found
                # Match illenkil error message show cheyyunnu
                
    except FileNotFoundError:
        # except = handles FileNotFoundError
        # Handles case when file doesn't exist
        # File illenkil varunna error handle cheyyunnu
        print("❌ File not found.")
        # print = output to console
        # Shows error message
        # File not found error message show cheyyunnu

def delete_record(filename, keyword):
    # Function to delete records containing keyword
    # File il ninnu specific keyword ulla records delete cheyyan ulla function
    
    try:
        # try = attempt code that might cause errors
        # Tries to delete from file
        # Error varumennu thonnunna code try block il idunnu
        
        with open(filename, "r") as f:
            # with open() = safe file opening for reading
            # filename = name of file to open
            # "r" = read mode
            # f = file object variable
            # Opens file to read existing records
            # Existing records read cheyyan file open cheyyunnu
            
            lines = f.readlines()
            # f.readlines() = reads all lines into list
            # lines = variable storing all lines
            # Reads all records into memory
            # Ella records um memory il store cheyyunnu
        
        with open(filename, "w") as f:
            # with open() = safe file opening for writing
            # filename = same file name
            # "w" = write mode - overwrites entire file
            # f = file object variable
            # Opens file in write mode (clears existing content)
            # File write mode il open cheyyunnu - existing content clear aavum
            
            for line in lines:
                # for loop = iterates through each saved line
                # line = current line from original file
                # Loops through all original records
                # Original file le ulla ella lines ilum loop cheyyunnu
                
                if keyword.lower() not in line.lower():
                    # if = conditional check
                    # keyword.lower() = keyword in lowercase
                    # not in = checks if keyword is NOT in line
                    # line.lower() = line in lowercase
                    # Only writes lines that don't contain the keyword
                    # Keyword illatha lines matram file il write cheyyunnu
                    
                    f.write(line)
                    # f.write() = write line to file
                    # line = current line that doesn't contain keyword
                    # Writes line back to file (keeps it)
                    # Keyword illatha lines file il write cheyyunnu (keep cheyyunnu)
        
        print("✅ Record deleted (if existed).")
        # print = output to console
        # ✅ = success emoji
        # Shows success message (even if record didn't exist)
        # Record delete aayi enna message show cheyyunnu - record undayirunnillenkilum
        
    except FileNotFoundError:
        # except = handles FileNotFoundError
        # Handles case when file doesn't exist
        # File illenkil varunna error handle cheyyunnu
        print("❌ File not found.")
        # print = output to console
        # Shows error message
        # File not found error message show cheyyunnu

# ==========================================================
# 🔹 9. Validation (Regex)
# ==========================================================
def validate_email(email):
    # Function to validate email format using regex
    # Email format correct aano enn check cheyyan ulla function - regex use cheythu
    
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)
    # return = returns True or False
    # re.match() = checks if pattern matches from start of string
    # r"" = raw string (treats backslashes literally)
    # ^ = start of string
    # [\w\.-]+ = one or more word characters, dots, or hyphens (username part)
    # @ = literal @ symbol
    # [\w\.-]+ = one or more word characters, dots, or hyphens (domain name)
    # \. = literal dot
    # \w+ = one or more word characters (extension like com, org)
    # $ = end of string
    # email = parameter to validate
    # Returns True if email format is valid, False otherwise
    # Email format correct aano enn check cheythu True/False return cheyyunnu

def validate_name(name):
    # Function to validate name contains only letters and spaces
    # Name il letters and spaces matram undo enn check cheyyan ulla function
    
    return re.match(r"^[A-Za-z ]+$", name)
    # return = returns True or False
    # re.match() = pattern matching from start
    # r"" = raw string
    # ^ = start of string
    # [A-Za-z ]+ = one or more uppercase letters, lowercase letters, or spaces
    # $ = end of string
    # name = parameter to validate
    # Returns True if name contains only letters and spaces
    # Name il letters and spaces matram undel True return cheyyunnu

def validate_phone(phone):
    # Function to validate phone number is exactly 10 digits
    # Phone number 10 digits aano enn check cheyyan ulla function
    
    return re.match(r"^\d{10}$", phone)
    # return = returns True or False
    # re.match() = pattern matching from start
    # r"" = raw string
    # ^ = start of string
    # \d{10} = exactly 10 digits
    # $ = end of string
    # phone = parameter to validate
    # Returns True if phone is exactly 10 digits
    # Phone number exactly 10 digits aayal True return cheyyunnu

# ==========================================================
# 🔹 10. Main Menu (User Input)
# ==========================================================
while True:
    # while True = infinite loop (runs forever until break)
    # Creates continuous menu system
    # Infinite loop - break varumbozhe stop aavum
    
    print("\n===============================")
    # print = output to console
    # \n = new line before printing
    # Prints decorative separator line
    # Decorative separator line print cheyyunnu
    
    print("    🧾 SMARTBIZ MANAGER SYSTEM")
    # print = output to console
    # 🧾 = emoji for document
    # Prints system title with emoji
    # System title emoji um koodi print cheyyunnu
    
    print("===============================")
    # print = output to console
    # Prints decorative separator line
    # Decorative separator line print cheyyunnu
    
    print("1️⃣ Add Employee")
    # print = output to console
    # 1️⃣ = emoji for number 1
    # Shows menu option 1 - Add Employee
    # Menu option 1 show cheyyunnu - Employee add cheyyan
    
    print("2️⃣ Add Manager")
    # Shows menu option 2 - Add Manager
    # Menu option 2 show cheyyunnu - Manager add cheyyan
    
    print("3️⃣ Add Sales Manager")
    # Shows menu option 3 - Add Sales Manager
    # Menu option 3 show cheyyunnu - Sales Manager add cheyyan
    
    print("4️⃣ Add Customer")
    # Shows menu option 4 - Add Customer
    # Menu option 4 show cheyyunnu - Customer add cheyyan
    
    print("5️⃣ View Records")
    # Shows menu option 5 - View Records
    # Menu option 5 show cheyyunnu - Records view cheyyan
    
    print("6️⃣ Search Records")
    # Shows menu option 6 - Search Records
    # Menu option 6 show cheyyunnu - Records search cheyyan
    
    print("7️⃣ Delete Record")
    # Shows menu option 7 - Delete Record
    # Menu option 7 show cheyyunnu - Record delete cheyyan
    
    print("8️⃣ Exit")
    # Shows menu option 8 - Exit program
    # Menu option 8 show cheyyunnu - Program exit cheyyan

    choice = input("Enter choice: ")
    # input() = gets user input from keyboard
    # "Enter choice: " = prompt message
    # choice = variable storing user's menu choice
    # Gets user's menu selection
    # User inte menu selection edukkan

    if choice == '1':
        # if = checks if choice is '1'
        # == '1' = string comparison for menu option 1
        # Executes when user selects Add Employee
        # User 1 select cheythal ee code execute aavum - Employee add cheyyan
        
        name = input("Enter Employee Name: ")
        # input() = gets user input
        # "Enter Employee Name: " = prompt message
        # name = variable storing employee name
        # Gets employee name from user
        # Employee name user ninnu edukkan
        
        if not validate_name(name): 
            # if not = checks if validate_name returns False
            # validate_name(name) = calls validation function
            # Validates that name contains only letters and spaces
            # Name valid aano enn check cheyyunnu - letters and spaces matram undel
            
            print("❌ Invalid name!"); 
            # print = output to console
            # ❌ = error emoji
            # Shows error message for invalid name
            # Name invalid enkil error message show cheyyunnu
            
            continue
            # continue = skips rest of loop and goes to next iteration
            # Goes back to menu without processing further
            # Loop le baaki code skip cheythu menu lekku povum
        
        email = input("Enter Email: ")
        # input() = gets user input
        # "Enter Email: " = prompt message
        # email = variable storing email address
        # Gets email from user
        # Email user ninnu edukkan
        
        if not validate_email(email): 
            # if not = checks if validate_email returns False
            # validate_email(email) = calls email validation function
            # Validates email format using regex
            # Email format correct aano enn check cheyyunnu
            
            print("❌ Invalid email!"); 
            # print = output to console
            # ❌ = error emoji
            # Shows error message for invalid email
            # Email invalid enkil error message show cheyyunnu
            
            continue
            # continue = skips rest and goes to next loop iteration
            # Menu lekku return aavum
            
        salary = float(input("Enter Salary: "))
        # input() = gets user input
        # float() = converts string input to decimal number
        # "Enter Salary: " = prompt message
        # salary = variable storing salary as decimal number
        # Gets salary and converts to float
        # Salary user ninnu eduthu float number aakki store cheyyunnu
        
        emp = Employee(name, email, salary)
        # Employee() = creates Employee object
        # name, email, salary = parameters for constructor
        # emp = variable storing new Employee object
        # Creates new Employee object with given details
        # Employee object create cheyyunnu - name, email, salary vechu
        
        emp.show_details()
        # emp.show_details() = calls show_details method on emp object
        # Shows all employee details
        # Employee details show cheyyunnu
        
        save_record("employees.txt", f"{emp.emp_id},{name},{email},{salary}")
        # save_record() = calls function to save to file
        # "employees.txt" = filename to save to
        # f"" = formatted string with employee data
        # emp.emp_id = employee ID from object
        # Saves employee record to file
        # Employee record file il save cheyyunnu

    elif choice == '2':
        # elif = else if - checks if choice is '2'
        # == '2' = string comparison for menu option 2
        # Executes when user selects Add Manager
        # User 2 select cheythal ee code execute aavum - Manager add cheyyan
        
        name = input("Enter Manager Name: ")
        # Gets manager name from user
        # Manager name user ninnu edukkan
        
        email = input("Enter Email: ")
        # Gets manager email from user
        # Manager email user ninnu edukkan
        
        salary = float(input("Enter Salary: "))
        # Gets manager salary and converts to float
        # Manager salary user ninnu eduthu float aakki store cheyyunnu
        
        dept = input("Enter Department: ")
        # Gets department name from user
        # Department name user ninnu edukkan
        
        m = Manager(name, email, salary, dept)
        # Manager() = creates Manager object
        # name, email, salary, dept = parameters
        # m = variable storing new Manager object
        # Creates new Manager object
        # Manager object create cheyyunnu
        
        m.show_details()
        # m.show_details() = calls show_details method
        # Shows all manager details
        # Manager details show cheyyunnu
        
        save_record("employees.txt", f"{m.emp_id},{name},{email},{salary},{dept}")
        # save_record() = saves manager record to file
        # "employees.txt" = filename
        # f"" = formatted string with manager data
        # Saves manager record
        # Manager record file il save cheyyunnu

    elif choice == '3':
        # elif = else if - checks if choice is '3'
        # == '3' = string comparison for menu option 3
        # Executes when user selects Add Sales Manager
        # User 3 select cheythal ee code execute aavum - Sales Manager add cheyyan
        
        name = input("Enter Sales Manager Name: ")
        # Gets sales manager name from user
        # Sales Manager name user ninnu edukkan
        
        email = input("Enter Email: ")
        # Gets sales manager email from user
        # Sales Manager email user ninnu edukkan
        
        salary = float(input("Enter Salary: "))
        # Gets sales manager salary and converts to float
        # Sales Manager salary user ninnu eduthu float aakki store cheyyunnu
        
        dept = input("Enter Department: ")
        # Gets department name from user
        # Department name user ninnu edukkan
        
        region = input("Enter Region: ")
        # Gets sales region from user
        # Sales region user ninnu edukkan
        
        sm = SalesManager(name, email, salary, dept, region)
        # SalesManager() = creates SalesManager object
        # name, email, salary, dept, region = parameters
        # sm = variable storing new SalesManager object
        # Creates new SalesManager object
        # SalesManager object create cheyyunnu
        
        sm.show_details()
        # sm.show_details() = calls show_details method
        # Shows all sales manager details
        # SalesManager details show cheyyunnu
        
        sm.record_sale(50000)
        # sm.record_sale() = calls record_sale method from SalesMixin
        # 50000 = example sale amount
        # Records a sample sale
        # Oru sample sale record cheyyunnu
        
        save_record("employees.txt", f"{sm.emp_id},{name},{email},{salary},{dept},{region}")
        # save_record() = saves sales manager record to file
        # "employees.txt" = filename
        # f"" = formatted string with all data
        # Saves sales manager record
        # SalesManager record file il save cheyyunnu

    elif choice == '4':
        # elif = else if - checks if choice is '4'
        # == '4' = string comparison for menu option 4
        # Executes when user selects Add Customer
        # User 4 select cheythal ee code execute aavum - Customer add cheyyan
        
        name = input("Enter Customer Name: ")
        # Gets customer name from user
        # Customer name user ninnu edukkan
        
        if not validate_name(name): 
            # Validates customer name
            # Customer name valid aano enn check cheyyunnu
            
            print("❌ Invalid name!"); 
            # Shows error for invalid name
            # Name invalid enkil error show cheyyunnu
            
            continue
            # Goes back to menu
            # Menu lekku return aavum
        
        email = input("Enter Email: ")
        # Gets customer email from user
        # Customer email user ninnu edukkan
        
        if not validate_email(email): 
            # Validates customer email
            # Customer email valid aano enn check cheyyunnu
            
            print("❌ Invalid email!"); 
            # Shows error for invalid email
            # Email invalid enkil error show cheyyunnu
            
            continue
            # Goes back to menu
            # Menu lekku return aavum
        
        phone = input("Enter Phone Number: ")
        # Gets customer phone number from user
        # Customer phone number user ninnu edukkan
        
        if not validate_phone(phone): 
            # Validates customer phone number
            # Customer phone valid aano enn check cheyyunnu
            
            print("❌ Invalid phone number!"); 
            # Shows error for invalid phone
            # Phone invalid enkil error show cheyyunnu
            
            continue
            # Goes back to menu
            # Menu lekku return aavum
        
        c = Customer(name, email, phone)
        # Customer() = creates Customer object
        # name, email, phone = parameters
        # c = variable storing new Customer object
        # Creates new Customer object
        # Customer object create cheyyunnu
        
        c.show_details()
        # c.show_details() = calls show_details method
        # Shows all customer details
        # Customer details show cheyyunnu
        
        save_record("customers.txt", f"{c.cust_id},{name},{email},{phone}")
        # save_record() = saves customer record to file
        # "customers.txt" = filename for customers
        # f"" = formatted string with customer data
        # Saves customer record
        # Customer record file il save cheyyunnu

    elif choice == '5':
        # elif = else if - checks if choice is '5'
        # == '5' = string comparison for menu option 5
        # Executes when user selects View Records
        # User 5 select cheythal ee code execute aavum - Records view cheyyan
        
        file = input("Enter file name (employees.txt/customers.txt): ")
        # input() = gets user input
        # Prompt asks for filename
        # file = variable storing filename
        # Gets filename from user
        # File name user ninnu edukkan
        
        view_records(file)
        # view_records() = calls function to view records
        # file = parameter with filename
        # Shows all records from specified file
        # Specify cheytha file le ulla records show cheyyunnu

    elif choice == '6':
        # elif = else if - checks if choice is '6'
        # == '6' = string comparison for menu option 6
        # Executes when user selects Search Records
        # User 6 select cheythal ee code execute aavum - Records search cheyyan
        
        file = input("Enter file name: ")
        # Gets filename from user
        # File name user ninnu edukkan
        
        keyword = input("Enter search keyword: ")
        # Gets search keyword from user
        # Search keyword user ninnu edukkan
        
        search_record(file, keyword)
        # search_record() = calls search function
        # file, keyword = parameters
        # Searches for records containing keyword
        # File il ninnu keyword ulla records kandu pidikkunnu

    elif choice == '7':
        # elif = else if - checks if choice is '7'
        # == '7' = string comparison for menu option 7
        # Executes when user selects Delete Record
        # User 7 select cheythal ee code execute aavum - Record delete cheyyan
        
        file = input("Enter file name: ")
        # Gets filename from user
        # File name user ninnu edukkan
        
        keyword = input("Enter keyword to delete: ")
        # Gets keyword for deletion from user
        # Delete cheyyan ulla keyword user ninnu edukkan
        
        delete_record(file, keyword)
        # delete_record() = calls delete function
        # file, keyword = parameters
        # Deletes records containing keyword
        # File il ninnu keyword ulla records delete cheyyunnu

    elif choice == '8':
        # elif = else if - checks if choice is '8'
        # == '8' = string comparison for menu option 8
        # Executes when user selects Exit
        # User 8 select cheythal ee code execute aavum - Program exit cheyyan
        
        print("👋 Thank you for using SmartBiz Manager!")
        # print = output to console
        # 👋 = waving hand emoji
        # Shows goodbye message
        # Goodbye message show cheyyunnu
        
        break
        # break = exits the while loop
        # Stops the program
        # Program stop cheyyunnu

    else:
        # else = executed when no other conditions match
        # Handles invalid menu choices
        # Invalid menu choice enkil ee code execute aavum
        
        print("❌ Invalid choice. Try again.")
        # print = output to console
        # ❌ = error emoji
        # Shows error message for invalid choice
        # Invalid choice enna error message show cheyyunnu
