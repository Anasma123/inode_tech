# ============================================================
# Example:  Hybrid Inheritance in Python
# Module 2 → Session 4
# ============================================================

# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_basic_info(self):
        print("\nName:", self.name)
        print("Age:", self.age)


# Derived Class 1 (inherits from Person)
class Student(Person):
    def __init__(self, name, age, course):
        # Call Person constructor directly
        Person.__init__(self, name, age)
        self.course = course

    def show_student_info(self):
        print("Course:", self.course)


# Derived Class 2 (inherits from Person)
class Employee(Person):
    def __init__(self, name, age, company, salary):
        # Call Person constructor directly
        Person.__init__(self, name, age)
        self.company = company
        self.salary = salary

    def show_employee_info(self):
        print("Company:", self.company)
        print("Salary:", self.salary)


# Hybrid Class (inherits from Student and Employee)
class WorkingStudent(Student, Employee):
    def __init__(self, name, age, course, company, salary, hours):
        # Explicitly call both parent constructors to avoid MRO issue
        Student.__init__(self, name, age, course)
        Employee.__init__(self, name, age, company, salary)
        self.hours = hours

    def show_full_info(self):
        print("\n====== Working Student Details ======")
        self.show_basic_info()
        self.show_student_info()
        self.show_employee_info()
        print("Working Hours per Week:", self.hours)
        print("=====================================")


# ---------- User Input ----------
name = input("Enter Name: ")
age = int(input("Enter Age: "))
course = input("Enter Course: ")
company = input("Enter Company Name: ")
salary = float(input("Enter Salary: "))
hours = int(input("Enter Weekly Working Hours: "))

# ---------- Object Creation ----------
ws = WorkingStudent(name, age, course, company, salary, hours)

# ---------- Display ----------
ws.show_full_info()
