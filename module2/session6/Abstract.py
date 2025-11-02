# ===============================================================
# 💡 Module 2 - Session 7
# Topic: Abstraction using Abstract Base Class (ABC)
# ===============================================================

# Import ABC and abstractmethod from the abc (Abstract Base Class) module
# ithu Pythonil abstract class create cheyyan vendi use cheyyunnu
from abc import ABC, abstractmethod


# ---------------------------------------------------------------
# 🔹 Abstract Base Class
# ---------------------------------------------------------------
class Shape(ABC):     # 'Shape' is an abstract class (blueprint for other shapes)
    
    # @abstractmethod → must be implemented by child classes
    @abstractmethod
    def area(self):
        # only method definition (no body)
        # ithu oru "template" mathram aanu — child il implement cheyyanam
        pass


# ---------------------------------------------------------------
# 🔹 Child Class 1 → Rectangle
# ---------------------------------------------------------------
class Rectangle(Shape):
    def __init__(self, l, w):
        # instance variables: length and width
        self.l = l
        self.w = w

    # override cheythu parentinte abstract method
    def area(self):
        # area formula → length * width
        return self.l * self.w


# ---------------------------------------------------------------
# 🔹 Child Class 2 → Circle
# ---------------------------------------------------------------
class Circle(Shape):
    def __init__(self, r):
        self.r = r  # radius

    def area(self):
        # area formula → πr²
        return 3.14 * self.r * self.r


# ---------------------------------------------------------------
# 🔹 User Input Section
# ---------------------------------------------------------------
print("1. Rectangle  2. Circle")
ch = int(input("Enter your choice (1 or 2): "))

# userinte choice anusarichu proper object create cheyyunnu
if ch == 1:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    obj = Rectangle(l, w)      # Rectangle object create cheythu
elif ch == 2:
    r = float(input("Enter radius: "))
    obj = Circle(r)            # Circle object create cheythu
else:
    print("Invalid choice!")
    exit()                     # program stop cheyyunnu if invalid

# ---------------------------------------------------------------
# 🔹 Display the Result
# ---------------------------------------------------------------
print("Area =", obj.area())    # polymorphism: area() works for both shapes
