# ==============================================================
# CLASS: Student
# Demonstrates difference between CLASS VARIABLE and INSTANCE VARIABLE
# ==============================================================

class Student:
    # Class Variable: shared among all objects
    school = "ABC Public School"     # same value for every student initially

    # Constructor (__init__): runs automatically when object is created
    def __init__(self, name, roll):
        # Instance Variables: unique for each object
        self.name = name             # stores student's name
        self.roll = roll             # stores student's roll number

    # Instance Method: displays details of each student
    def show(self):
        # Access instance variables using self
        print("Name:", self.name)
        print("Roll:", self.roll)
        # Access class variable using ClassName
        print("School:", Student.school)
        print("-------------------------")


# ==============================================================
# OBJECT CREATION
# ==============================================================

# Two different Student objects created with unique data
s1 = Student("Anas", 101)
s2 = Student("Fathima", 102)

# Each object has its own name & roll, but both share the same school
s1.show()
s2.show()

# ==============================================================
# MODIFY CLASS VARIABLE
# ==============================================================

# Changing class variable using ClassName
# This change reflects for ALL objects (since it's shared)
Student.school = "XYZ Model School"

# Display again after modification
s1.show()
s2.show()
