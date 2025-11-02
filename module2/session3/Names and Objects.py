# ============================================================
# Example: Understanding Object References in Python
# Module 2 → Session 3: Names and Objects
# ============================================================

class Student:
    def __init__(self, name):
        self.name = name   # instance variable (unique for each object)

# Create object s1 → refers to a Student object in memory
s1 = Student("Anas")

# Create another object s3 (independent)
s3 = Student("Fathima")

# Assign s2 to refer to same object as s1
s2 = s1   # both now point to the SAME object in memory

# Now if we change s2.name, it will also affect s1.name (since both are same object)
s2.name = "Rahul"

# Display values
print("s1.name =", s1.name)   # Rahul (changed through s2)
print("s2.name =", s2.name)   # Rahul (same reference)
print("s3.name =", s3.name)   # Fathima (different object)
