# ============================================================
# Example: Single Inheritance with User Input
# Module 2 → Session 4: Inheritance
# ============================================================

class Person:
    def __init__(self, name, age, address):
        # Constructor of parent class (Person)
        # self.name, self.age, self.address → ivide objectinte attributes store cheyyunnu
        self.name = name
        self.age = age
        self.address = address
        print("Parent class constructor called")

class Student(Person):
    def __init__(self, name, age, address, course):
        # super() → parent classinte constructor call cheyyan
        # ivide parentinte name, age, address assign cheyyunnu
        super().__init__(name, age, address)

        # Child classinte thante own attribute aanu course
        self.course = course
        print("Child class constructor called")

    def show_info(self):
        # Objectinte ella details display cheyyunna function
        print("\nName:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)
        print("Course:", self.course)

# ---------- User Input Section ----------
name = input("Enter Name: ")
age = int(input("Enter Age: "))
address = input("Enter Address: ")
course = input("Enter Course: ")

# ---------- Object Creation ----------
s1 = Student(name, age, address, course)
# Student object create cheyyumbol:
#   1️⃣ Parent class constructor run aavum
#   2️⃣ Pinne child class constructor run aavum

# ---------- Display Student Info ----------
s1.show_info()
