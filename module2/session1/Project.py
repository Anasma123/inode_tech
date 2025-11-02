# Program: Create a Student Information System using Classes and Objects in Python

# -------------------------------
# Class Definition
# -------------------------------
# The 'Student' class represents each student's basic information.
# It includes a constructor to initialize data and a method to display it.

class Student:
    # Constructor to initialize student details
    def __init__(self, name, age, grade):
        self.name = name       # Student name
        self.age = age         # Student age
        self.grade = grade     # Student grade

    # Method to display student information
    def show_info(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)
        print("------------------------")


# -------------------------------
# Object Creation
# -------------------------------
# Creating multiple student objects with different data
student1 = Student("Anas", 20, "A")
student2 = Student("Fathima", 21, "B+")
student3 = Student("Rahul", 22, "A+")


# -------------------------------
# Displaying Student Information
# -------------------------------
# Calling the show_info() method for each student object
student1.show_info()
student2.show_info()
student3.show_info()
