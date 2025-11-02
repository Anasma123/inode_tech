# ===============================================================
# 💡 Module 2 - Session 7
# Topic: Abstraction using Abstract Base Class (ABC) and @abstractmethod
# ===============================================================

# Import ABC and abstractmethod
# ithu use cheythu abstract class create cheyyam (cannot be instantiated directly)
from abc import ABC, abstractmethod


# ---------------------------------------------------------------
# 🔹 Abstract Base Class
# ---------------------------------------------------------------
class Vehicle(ABC):   # parent abstract class
    # abstractmethod → all subclasses must define this method
    @abstractmethod
    def fuel_efficiency(self):
        # only method structure / declaration
        # implementation child classil aanu cheyyendath
        pass


# ---------------------------------------------------------------
# 🔹 Child Class 1 → Car
# ---------------------------------------------------------------
class Car(Vehicle):
    # define cheyyunnu abstract method parentil ninn
    def fuel_efficiency(self):
        return "Car mileage: 15 km/l"   # simple return statement


# ---------------------------------------------------------------
# 🔹 Child Class 2 → Bike
# ---------------------------------------------------------------
class Bike(Vehicle):
    # child class implements parentinte method
    def fuel_efficiency(self):
        return "Bike mileage: 40 km/l"


# ---------------------------------------------------------------
# 🔹 User Input Section
# ---------------------------------------------------------------
print("Choose Vehicle Type:")
print("1. Car")
print("2. Bike")

choice = int(input("Enter your choice (1 or 2): "))

# ---------------------------------------------------------------
# 🔹 Object Creation based on user choice
# ---------------------------------------------------------------
if choice == 1:
    v = Car()    # Car object create cheythu
elif choice == 2:
    v = Bike()   # Bike object create cheythu
else:
    print("Invalid choice!")
    exit()

# ---------------------------------------------------------------
# 🔹 Display Result (Polymorphism)
# ---------------------------------------------------------------
# ithil v.fuel_efficiency() works differently for each vehicle type
print(v.fuel_efficiency())
