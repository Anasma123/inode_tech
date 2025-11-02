# Example 1: Simple Class and Object

# -------------------------------
# Class Definition
# -------------------------------
# A class is a blueprint for creating objects.
# Here, 'Car' represents a generic car model.
class Car:
    # Constructor method (called automatically when an object is created)
    def __init__(self, brand, color):
        # 'self' refers to the current object
        # Instance variables (unique data for each object)
        self.brand = brand
        self.color = color

    # Method to display car details
    def show_details(self):
        print("Brand:", self.brand)
        print("Color:", self.color)


# -------------------------------
# Object Creation
# -------------------------------
# Each object represents one car with its own data
car1 = Car("BMW", "Black")      # creates object car1
car2 = Car("Suzuki", "White")   # creates object car2


# -------------------------------
# Method Calling
# -------------------------------
# Calling 'show_details()' displays data of each object
car1.show_details()
car2.show_details()
