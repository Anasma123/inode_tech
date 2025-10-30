# Mini Project: Student Info System

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def show_info(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)
        print("------------------------")

# Creating 3 student objects
student1 = Student("Anas", 20, "A")
student2 = Student("Fathima", 21, "B+")
student3 = Student("Rahul", 22, "A+")

# Displaying info
student1.show_info()
student2.show_info()
student3.show_info()
