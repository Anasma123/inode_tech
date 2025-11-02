# ==============================================================
# MODULE 2 → SESSION 2
# COMPLETE EXAMPLE: Company Employee Management System
# Covers: Class Variables, Instance Variables, @classmethod,
#         @staticmethod, Object Counter, User Input, Update Display
# ==============================================================

class Employee:
    # ------------------------------
    # CLASS VARIABLES (common for all objects)
    # ------------------------------
    company_name = "iNode Tech Pvt Ltd"   # shared company name
    total_employees = 0                   # total employee counter
    total_salary_expense = 0              # total salary of all employees

    # ==============================================================
    # CONSTRUCTOR: initializes data for each employee (instance)
    # ==============================================================
    def __init__(self, name, emp_id, department, salary):
        # 'self' → represents the current object
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

        # update shared (class-level) data
        Employee.total_employees += 1
        Employee.total_salary_expense += salary

    # ==============================================================
    # INSTANCE METHOD: shows individual employee details
    # ==============================================================
    def show_employee_details(self):
        print("\n--------------------------------------")
        print("Employee Name     :", self.name)
        print("Employee ID       :", self.emp_id)
        print("Department        :", self.department)
        print("Salary (₹)        :", self.salary)
        print("Company           :", Employee.company_name)
        print("--------------------------------------")

    # ==============================================================
    # CLASS METHOD: displays company-level data (shared by all)
    # ==============================================================
    @classmethod
    def company_summary(cls):
        print("\n========== COMPANY SUMMARY ==========")
        print("Company Name           :", cls.company_name)
        print("Total Employees         :", cls.total_employees)
        print("Total Salary Expense (₹):", cls.total_salary_expense)
        print("=====================================")

    # ==============================================================
    # STATIC METHOD: shows a company rule or general info
    # ==============================================================
    @staticmethod
    def company_policy():
        print("\n[Company Policy]")
        print("➡ All employees must submit attendance before 10:00 AM.")
        print("➡ Maintain discipline, dedication, and teamwork always!")

    # ==============================================================
    # CLASS METHOD: updates company name (shared variable)
    # ==============================================================    
    @classmethod
    def change_company_name(cls, new_name, employee_list):
        """
        Changes company name for all employees (since it's shared).
        Then displays updated details and summary immediately.
        """
        old_name = cls.company_name
        cls.company_name = new_name
        print(f"\n✅ Company name changed from '{old_name}' to '{new_name}' successfully.")

        # Now re-display all employee data with the new company name
        print("\n🔁 Displaying all employee details with updated company name...")
        for e in employee_list:
            e.show_employee_details()

        # Also show updated company summary
        cls.company_summary()


# ==============================================================
# USER INPUT SECTION
# ==============================================================

print("===== EMPLOYEE MANAGEMENT SYSTEM =====")
n = int(input("Enter the number of employees to add: "))

# create list to store employee objects
employee_list = []

# get details for each employee
for i in range(n):
    print(f"\nEnter details for Employee {i+1}:")
    name = input("Enter Employee Name: ")
    emp_id = input("Enter Employee ID: ")
    department = input("Enter Department: ")

    # input validation for salary
    while True:
        try:
            salary = float(input("Enter Salary (₹): "))
            if salary < 0:
                print("❌ Salary cannot be negative. Enter again.")
            else:
                break
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

    # create new object and add to list
    emp = Employee(name, emp_id, department, salary)
    employee_list.append(emp)

# ==============================================================
# DISPLAY EMPLOYEE DETAILS AND COMPANY SUMMARY
# ==============================================================

print("\n===== EMPLOYEE DETAILS =====")
for e in employee_list:
    e.show_employee_details()

# show shared info and rules
Employee.company_summary()
Employee.company_policy()

# ==============================================================
# OPTIONAL: CHANGE COMPANY NAME
# ==============================================================

ch = input("\nDo you want to change the company name? (yes/no): ").lower()

if ch == "yes":
    new_name = input("Enter new company name: ")
    # class method call (also refreshes display)
    Employee.change_company_name(new_name, employee_list)
else:
    print("\n✅ Company name unchanged.")
    Employee.company_summary()

print("\nProgram Execution Completed Successfully ✅")
