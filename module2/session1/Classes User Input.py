# Program: Calculate Total and Average Marks of a Student using Classes and User Input in Python

# -------------------------------
# Class Definition
# -------------------------------
# The 'Student' class stores the name and marks of a student
# and calculates the total and average marks.

class Student:
    # Constructor to initialize student name and marks
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name      # Student name
        self.mark1 = mark1    # Mark for subject 1
        self.mark2 = mark2    # Mark for subject 2
        self.mark3 = mark3    # Mark for subject 3

    # Method to display student details, total, and average
    def display_details(self):
        total = self.mark1 + self.mark2 + self.mark3
        average = total / 3
        print("\nStudent Name:", self.name)
        print("Total Marks:", total)
        print("Average Marks:", average)
        print("------------------------")


# -------------------------------
# User Input Section
# -------------------------------
# Taking student details and marks from user
name = input("Enter student name: ")
m1 = int(input("Enter mark 1: "))
m2 = int(input("Enter mark 2: "))
m3 = int(input("Enter mark 3: "))

# -------------------------------
# Object Creation
# -------------------------------
# Creating a 'Student' object using user input data
student = Student(name, m1, m2, m3)

# -------------------------------
# Displaying Output
# -------------------------------
# Calling method to show total and average
student.display_details()
