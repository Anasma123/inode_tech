# ==============================================================
# CLASS: Employee
# Demonstrates CLASS and INSTANCE variables with an automatic counter
# ==============================================================

class Employee:
    company = "iNode Tech"     # Class variable → same for all employees
    emp_count = 0              # Class variable → keeps track of total employees

    # Constructor: initializes instance variables
    def __init__(self, name, salary):
        self.name = name            # Instance variable → employee name
        self.salary = salary        # Instance variable → employee salary
        Employee.emp_count += 1     # Increment shared counter every time object created

    # Method to display each employee’s information
    def display(self):
        print("Employee Name:", self.name)               # Access instance variable
        print("Salary:", self.salary)                    # Access instance variable
        print("Company:", Employee.company)              # Access class variable
        print("-------------------------")


# ==============================================================
# OBJECT CREATION
# ==============================================================

# Creating multiple employee objects (each has unique name & salary)
e1 = Employee("Anas", 25000)
e2 = Employee("Fathima", 30000)
e3 = Employee("Rahul", 28000)

# ==============================================================
# DISPLAY EMPLOYEE DETAILS
# ==============================================================

# Calling display() for each object
e1.display()
e2.display()
e3.display()

# ==============================================================
# DISPLAY TOTAL COUNT
# ==============================================================

# Access class variable using ClassName to show shared counter
print("Total Employees in Company:", Employee.emp_count)
