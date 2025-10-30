# Global variable
school_name = input("Enter the Global School Name: ")

class Student:
    def __init__(self, name):
        self.name = name

    def show_global_school(self):
        # Uses the global variable directly
        print(self.name, "studies in", school_name)

    def redefine_school(self):
        # Local variable with same name (taken from user)
        school_name = input("Enter a new Local School Name for this student: ")
        print(self.name, "studies in", school_name)


# ---------- Create Object from User Input ----------
student_name = input("\nEnter Student Name: ")
s1 = Student(student_name)

print("\n---- Using Global Variable ----")
s1.show_global_school()

print("\n---- After Redefining Inside Method ----")
s1.redefine_school()

print("\nOutside class (Global School):", school_name)
