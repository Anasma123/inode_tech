# ============================================================
# Example: Global vs Local Variable with Same Name in Class
# Module 2 → Session 3: Python Scopes and Namespaces
# ============================================================

# -----------------------------
# GLOBAL VARIABLE (defined outside class)
# -----------------------------
school_name = "ABC Public School"
# → This is a global variable.
# → It can be accessed anywhere in this file unless hidden by a local variable.
# Manglish: Ithu global aanu, functionum classum okke ullil ninn access cheyyam.

class Student:
    def __init__(self, name):
        # Instance variable (unique for each object)
        self.name = name
        # Manglish: Ithu oru objectine mathramulla variable aanu (per student).

    # -----------------------------------------------------------
    # Method 1: Accessing the GLOBAL VARIABLE directly
    # -----------------------------------------------------------
    def show_global_school(self):
        # Here, no local variable named 'school_name' exists.
        # So Python looks for 'school_name' in global scope.
        print(self.name, "studies in", school_name)
        #  Ithu global variable use cheyyunnu (ABC Public School).

    # -----------------------------------------------------------
    # Method 2: Redefining a LOCAL VARIABLE with the same name
    # -----------------------------------------------------------
    def redefine_school(self):
        # Local variable (new variable inside this function)
        school_name = "XYZ Model School"
        # This hides the global variable temporarily inside this method.
        print(self.name, "studies in", school_name)
        #  Ithu oru local variable aanu — global name pole undenkilum,
        # function ullil athaanu use aavuka (XYZ Model School).
        # Global variable purath unchanged aanu.

# -----------------------------------------------------------
# OBJECT CREATION
# -----------------------------------------------------------

s1 = Student("Anas")   # creates one student object

# -----------------------------------------------------------
# METHOD CALLS
# -----------------------------------------------------------

print("---- Using Global Variable ----")
s1.show_global_school()   # uses global school_name (ABC Public School)

print("\n---- After Redefining Inside Method ----")
s1.redefine_school()      # uses local school_name (XYZ Model School)

# -----------------------------------------------------------
# CHECK THE GLOBAL VARIABLE OUTSIDE CLASS
# -----------------------------------------------------------
print("\nOutside class (global):", school_name)
# prints ABC Public School — shows that global variable is unchanged
