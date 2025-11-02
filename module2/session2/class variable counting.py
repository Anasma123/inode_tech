# ==============================================================
# CLASS: Student
# Demonstrates use of CLASS VARIABLE to count total number of objects
# ==============================================================

class Student:
    count = 0        # Class variable — shared among all Student objects

    # Constructor (__init__) runs automatically when object is created
    def __init__(self, name):
        self.name = name        # Instance variable (unique for each object)
        Student.count += 1      # Increment class variable every time a new object is created

    # Instance Method — to display student name
    def show(self):
        print("Student Name:", self.name)


# ==============================================================
# OBJECT CREATION
# ==============================================================

# Creating multiple Student objects
s1 = Student("Anas")       # count = 1
s2 = Student("Fathima")    # count = 2
s3 = Student("Rahul")      # count = 3

# ==============================================================
# DISPLAY SECTION
# ==============================================================

# Call method for each object
s1.show()
s2.show()
s3.show()

# Accessing class variable using ClassName
print("Total Students:", Student.count)
