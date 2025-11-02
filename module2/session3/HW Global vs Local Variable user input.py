# ============================================================
# Example: Global vs Local Variable with User Input
# Module 2 → Session 3: Python Scopes and Namespaces
# ============================================================

# ------------------------------------------------------------
# Step 1️⃣: GLOBAL VARIABLE (with user input)
# ------------------------------------------------------------
school_name = input("Enter the Global School Name: ")
# This variable is defined outside any class/function → so it's GLOBAL.
#  Ithu global variable aanu, program muzhuvanilum use cheyyam.

class Student:
    def __init__(self, name):
        # Instance variable (unique per student object)
        self.name = name
        #  Ithu prathi studentinte peru store cheyyan aanu.

    # --------------------------------------------------------
    # Step 2️⃣: Using the GLOBAL variable inside a method
    # --------------------------------------------------------
    def show_global_school(self):
        # No local variable 'school_name' here.
        # So Python looks for it in the global namespace.
        print(self.name, "studies in", school_name)
        # Ithu global school_name use cheyyunnu (user input vech).

    # --------------------------------------------------------
    # Step 3️⃣: Redefining a LOCAL variable with same name
    # --------------------------------------------------------
    def redefine_school(self):
        # Local variable with same name as global
        school_name = input("Enter a new Local School Name for this student: ")
        # This 'school_name' exists only inside this function.
        print(self.name, "studies in", school_name)
        #  Ithu local variable aanu, ath global school_name hide cheyyum.
        # Global variable purath unchanged aanu.

# ------------------------------------------------------------
# Step 4️⃣: CREATE OBJECT USING USER INPUT
# ------------------------------------------------------------
student_name = input("\nEnter Student Name: ")
s1 = Student(student_name)
#  user ninnu student name eduthu, object create cheythu.

# ------------------------------------------------------------
# Step 5️⃣: METHOD CALLS
# ------------------------------------------------------------

print("\n---- Using Global Variable ----")
s1.show_global_school()   # uses global variable entered by user

print("\n---- After Redefining Inside Method ----")
s1.redefine_school()      # creates a local variable (new name from user)

# ------------------------------------------------------------
# Step 6️⃣: DISPLAY GLOBAL VARIABLE OUTSIDE CLASS
# ------------------------------------------------------------
print("\nOutside class (Global School):", school_name)
#  Purathulla global variable unchanged aayi thanne undu.
