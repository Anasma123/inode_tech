# ============================================================
# Example: Method Overriding and Polymorphism using Shapes
# Module 2 → Session 5
# ============================================================

import math   # Import math module for π (pi) constant

# ---------- Base Class ----------
class Shape:
    def area(self):
        # Base class method — general message only
        # Ee base class area() method just oru placeholder aanu.
        print("This is a generic shape")


# ---------- Child Class 1 ----------
class Rectangle(Shape):
    def __init__(self, length, width):
        # Initialize length and width
        # Ee constructor length, width values store cheyyunnu.
        self.length = length
        self.width = width

    def area(self):
        # Overrides base class method
        # Ee method rectangleinte area calculate cheyyum (L * W)
        return self.length * self.width


# ---------- Child Class 2 ----------
class Circle(Shape):
    def __init__(self, radius):
        # Initialize radius
        # Ee constructor circleinte radius save cheyyunnu
        self.radius = radius

    def area(self):
        # Overrides base class method
        # Ee method circleinte area calculate cheyyum (πr²)
        return math.pi * self.radius ** 2


# ---------- User Input Section ----------
print("1. Rectangle  2. Circle")
choice = int(input("Enter your choice: "))

# Based on user choice, object create cheyyunnu
if choice == 1:
    l = float(input("Enter Length: "))
    w = float(input("Enter Width: "))
    shape = Rectangle(l, w)  # Rectangle object create cheyyunnu
elif choice == 2:
    r = float(input("Enter Radius: "))
    shape = Circle(r)        # Circle object create cheyyunnu
else:
    shape = Shape()          # Invalid choice → base class object

# ---------- Display Result ----------
# Ee line polymorphism kaanikunnu — same function name (area)
# pakshe behavior vary cheyyunnu object type prakarum.
print("Area =", shape.area())
