# ============================================================
# Module 2 → Session 3
# Topic: Python Scopes, Namespaces, LEGB Rule & Object References
# ============================================================

# ---------- Global Variables ----------
school_name = input("Enter the Global School Name: ")
count = 0
# Program startil global variables define cheythu – ivide randu global variables undu

print("\n--- Program Start ---")

def outer_function():
    # ---------- Enclosing Function ----------
    trainer = input("\nEnter Trainer Name: ")
    x = int(input("Enter starting value of enclosing variable x: "))
    print("\nInside outer_function()")
    print("Trainer:", trainer)

    def inner_function():
        # ---------- Local Scope ----------
        topic = input("\nEnter training topic (Local Variable): ")
        y = int(input("Enter local number y: "))
        print("\nInside inner_function()")
        print("Topic:", topic)

        # Accessing and modifying enclosing variable using nonlocal
        nonlocal x
        x += 10
        print("Updated enclosing variable x:", x)
        # nonlocal use cheythath kond outer_function() ilulla x modify aayi

        # Accessing and modifying global variable using global keyword
        global count
        count += 1
        print("Updated global variable count:", count)
        # global use cheythath kond purathulla count update aayi

        # Local namespace display cheyyunnu
        print("\nLocal Namespace (inner_function):", locals())

    # inner_function() call
    inner_function()

    # After calling inner function
    print("\nAfter inner_function() call, Enclosing variable x =", x)
    # Enclosing x nonlocal keyword kond updated aayi

    # Display outer_function() namespace
    print("\nLocal Namespace (outer_function):", locals())

# outer_function() call
outer_function()

print("\n--- Outside all functions ---")
print("Global Namespace Keys:", list(globals().keys())[:10])  # limiting to first 10 for clarity
# globals().keys() → global variables, functions, classes okke list cheyyum

print("Global count =", count)
print("Global school_name =", school_name)

# ---------- Demonstrating Object Reference ----------
print("\n--- Object Reference Example ---")

class Student:
    def __init__(self, name):
        self.name = name

# Object create cheyyunnu user input kond
name1 = input("Enter first student name: ")
s1 = Student(name1)
# s1 oru object aanu, ithinte memory address store aayittund

s2 = s1   # s2 um athae object ne refer cheyyunnu
print("\nBefore change:")
print("s1 name:", s1.name)
print("s2 name:", s2.name)

# Modify object using s2
new_name = input("\nEnter new name to update using s2: ")
s2.name = new_name
print("\nAfter change through s2:")
print("s1 name:", s1.name)
print("s2 name:", s2.name)

# id() → memory address kaanikkum
print("\nMemory Address of s1:", id(s1))
print("Memory Address of s2:", id(s2))
print("✅ Both same → same object in memory")

# ---------- LEGB Rule Demonstration ----------
print("\n--- LEGB Rule Example ---")

x = input("Enter a value for global x: ")

def outer():
    x = input("Enter a value for enclosing x (inside outer): ")
    def inner():
        x = input("Enter a value for local x (inside inner): ")
        print("Inside inner():", x)  # Local variable used here
    inner()
    print("Inside outer():", x)      # Enclosing variable visible here

outer()
print("Outside function:", x)        # Global variable visible here

print("\n--- Program End ---")
