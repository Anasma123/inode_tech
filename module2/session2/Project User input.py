# ==============================================================
# CLASS: Employee
# Demonstrates CLASS and INSTANCE variables with USER INPUT and COUNTER
# ==============================================================

class Employee:
    company = "iNode Tech"   # class variable → same for all employees
    emp_count = 0            # class variable → shared counter for total employees

    # Constructor: initializes instance variables and updates counter
    def __init__(self, name, salary):
        self.name = name              # instance variable → employee name (unique for each object)
        self.salary = salary          # instance variable → salary (unique for each object)
        Employee.emp_count += 1       # increases counter every time a new employee object is created

    # Method to display employee details
    def display(self):
        print("\nEmployee Name:", self.name)          # print instance variable 'name'
        print("Salary:", self.salary)                 # print instance variable 'salary'
        print("Company:", Employee.company)           # access class variable using class name
        print("---------------------------")          # separator line for readability


# ==============================================================
# USER INPUT SECTION
# ==============================================================

# Ask user how many employees to add
n = int(input("Enter number of employees: "))

# Create an empty list to store all employee objects
employees = []

# Loop runs 'n' times to collect details for each employee
for i in range(n):
    # Print which employee details are being entered
    # \n → adds new line for spacing
    # f-string used to dynamically insert employee number (i+1)
    print(f"\nEnter details for Employee {i+1}:")
    
    # Take input for name and salary
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))

    # Create an Employee object using user input
    emp = Employee(name, salary)
    
    # Add the new object to the list
    employees.append(emp)


# ==============================================================
# DISPLAY EMPLOYEE DETAILS
# ==============================================================

# Loop through each employee object and call the display() method
for e in employees:
    e.display()

# Print total number of employees created
# Access the class variable directly using ClassName
print("Total Employees in Company:", Employee.emp_count)
