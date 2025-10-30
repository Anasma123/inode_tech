class Employee:
    company = "iNode Tech"   # class variable (common)
    emp_count = 0            # class variable (shared counter)

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1   # increase when new employee created

    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", Employee.company)
        print("-------------------------")

# creating objects
e1 = Employee("Anas", 25000)
e2 = Employee("Fathima", 30000)
e3 = Employee("Rahul", 28000)

# displaying employee info
e1.display()
e2.display()
e3.display()

print("Total Employees in Company:", Employee.emp_count)
