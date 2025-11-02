# ============================================================
# MODULE 2 → SESSION 4
# Topic: Inheritance in Python (Full Concept)
# ============================================================

# ------------------------------------------------------------
# 1️⃣ SINGLE INHERITANCE
# ------------------------------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_basic_info(self):
        print("\n[Single Inheritance Example]")
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):   # Student inherits from Person
    def __init__(self, name, age, course):
        # Directly call Person constructor (not super())
        Person.__init__(self, name, age)
        self.course = course

    def show_student_info(self):
        print("Course:", self.course)


# ------------------------------------------------------------
# 2️⃣ MULTILEVEL INHERITANCE
# ------------------------------------------------------------
class GraduateStudent(Student):  # inherits from Student → Person
    def __init__(self, name, age, course, thesis):
        # Call parent directly
        Student.__init__(self, name, age, course)
        self.thesis = thesis

    def show_thesis(self):
        print("\n[Multilevel Inheritance Example]")
        print("Thesis Title:", self.thesis)


# ------------------------------------------------------------
# 3️⃣ MULTIPLE INHERITANCE
# ------------------------------------------------------------
class Athlete:
    def play(self):
        print("\n[Multiple Inheritance Example]")
        print("Athlete is playing football...")


class Scholar(Student, Athlete):  # inherits from Student + Athlete
    def __init__(self, name, age, course):
        Student.__init__(self, name, age, course)

    def show_role(self):
        print("Scholar is both a student and an athlete!")


# ------------------------------------------------------------
# 4️⃣ HIERARCHICAL INHERITANCE
# ------------------------------------------------------------
class Teacher(Person):  # Another child of Person
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)
        self.subject = subject

    def show_teacher_info(self):
        print("\n[Hierarchical Inheritance Example]")
        print("Subject:", self.subject)


# ------------------------------------------------------------
# 5️⃣ HYBRID INHERITANCE
# ------------------------------------------------------------
class Employee(Person):  # inherits from Person
    def __init__(self, name, age, company, salary):
        Person.__init__(self, name, age)
        self.company = company
        self.salary = salary

    def show_employee_info(self):
        print("Company:", self.company)
        print("Salary:", self.salary)


class WorkingStudent(Student, Employee):  # Hybrid inheritance
    def __init__(self, name, age, course, company, salary, hours):
        # Call all parent constructors directly (not super())
        Student.__init__(self, name, age, course)
        Employee.__init__(self, name, age, company, salary)
        self.hours = hours

    def show_full_info(self):
        print("\n[Hybrid Inheritance Example]")
        print("====== Working Student Details ======")
        self.show_basic_info()
        self.show_student_info()
        self.show_employee_info()
        print("Working Hours:", self.hours)
        print("=====================================")


# ------------------------------------------------------------
# 6️⃣ METHOD OVERRIDING
# ------------------------------------------------------------
class Animal:
    def sound(self):
        print("\nAnimal makes a sound")

class Dog(Animal):
    def sound(self):
        print("\nDog barks: Woof Woof!")


# ------------------------------------------------------------
# ---------- USER INPUT SECTION ----------
# ------------------------------------------------------------
print("=== ENTER DETAILS FOR ALL EXAMPLES ===")
name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
course = input("Enter your Course: ")
thesis = input("Enter Thesis Title: ")
subject = input("Enter Subject (for Teacher): ")
company = input("Enter Company Name: ")
salary = float(input("Enter Salary: "))
hours = int(input("Enter Weekly Working Hours: "))

# ------------------------------------------------------------
# ---------- OBJECT CREATION ----------
# ------------------------------------------------------------
# 1️⃣ Single Inheritance
s1 = Student(name, age, course)
s1.show_basic_info()
s1.show_student_info()

# 2️⃣ Multilevel Inheritance
g1 = GraduateStudent(name, age, course, thesis)
g1.show_thesis()

# 3️⃣ Multiple Inheritance
sc = Scholar(name, age, course)
sc.show_role()
sc.play()

# 4️⃣ Hierarchical Inheritance
t1 = Teacher(name, age, subject)
t1.show_teacher_info()

# 5️⃣ Hybrid Inheritance
ws = WorkingStudent(name, age, course, company, salary, hours)
ws.show_full_info()

# 6️⃣ Method Overriding
a = Animal()
d = Dog()
a.sound()
d.sound()
