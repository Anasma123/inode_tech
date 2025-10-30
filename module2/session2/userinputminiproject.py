class Employee:
    company = "iNode Tech"   # class variable
    emp_count = 0            # shared counter

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display(self):
        print("\nEmployee Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", Employee.company)
        print("---------------------------")


# ---------- User Input Section ----------
n = int(input("Enter number of employees: "))
employees = []

for i in range(n):
    print(f"\nEnter details for Employee {i+1}:")
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))
    emp = Employee(name, salary)
    employees.append(emp)

# ---------- Display Employee Details ----------
for e in employees:
    e.display()

print("Total Employees in Company:", Employee.emp_count)
