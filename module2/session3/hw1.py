# Global variable
school_name = "ABC Public School"

class Student:
    def __init__(self, name):
        self.name = name

    def show_global_school(self):
        # Using the global variable directly
        print(self.name, "studies in", school_name)

    def redefine_school(self):
        # Local variable with same name
        school_name = "XYZ Model School"
        print(self.name, "studies in", school_name)


# Creating object
s1 = Student("Anas")

print("---- Using Global Variable ----")
s1.show_global_school()

print("\n---- After Redefining Inside Method ----")
s1.redefine_school()

print("\nOutside class (global):", school_name)
