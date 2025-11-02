# ============================================================
# Example: Polymorphism and Method Overriding in Python
# Module 2 → Session 5
# ============================================================

# ---------- Base Class ----------
class Employee:
    def calculate_salary(self):
        # Base class method — general employee (no details)
        # Ee method oru general employee ne represent cheyyunnu
        print("This is a generic employee. Salary details not available.")


# ---------- Child Class 1 ----------
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        # Overrides the parent method with a specific implementation
        # Ee method parent method ne replace cheythu, full-time salary define cheyyunnu
        salary = 40000
        print("Salary =", salary)


# ---------- Child Class 2 ----------
class PartTimeEmployee(Employee):
    def calculate_salary(self):
        # Overrides the parent method again
        # Ee method part-time employeeinte salary display cheyyunnu
        salary = 10000
        print("Salary =", salary)


# ---------- User Input ----------
emp_type = input("Enter employee type (FullTime / PartTime): ")
# User ninn employee type edukkunnu
# Input fulltime aanenkil FullTimeEmployee() object create cheyyum
# Input parttime aanenkil PartTimeEmployee() object create cheyyum

# ---------- Polymorphism in Action ----------
if emp_type.lower() == "fulltime":
    emp = FullTimeEmployee()
elif emp_type.lower() == "parttime":
    emp = PartTimeEmployee()
else:
    emp = Employee()

# Calling the same method, but the result depends on the object
# Polymorphism kaanikunnu — oru method name aanu, pakshe behavior vary cheyyum
emp.calculate_salary()
