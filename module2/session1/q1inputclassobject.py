class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def display_details(self):
        total = self.mark1 + self.mark2 + self.mark3
        average = total / 3
        print("\nStudent Name:", self.name)
        print("Total Marks:", total)
        print("Average Marks:", average)
        print("------------------------")

# Taking input from user
name = input("Enter student name: ")
m1 = int(input("Enter mark 1: "))
m2 = int(input("Enter mark 2: "))
m3 = int(input("Enter mark 3: "))

# Creating object
student = Student(name, m1, m2, m3)

# Display details
student.display_details()
