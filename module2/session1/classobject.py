# Example 1: Simple Class and Object
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show_details(self):
        print("Brand:", self.brand)
        print("Color:", self.color)

# Creating objects
car1 = Car("BMW", "Black")
car2 = Car("Suzuki", "White")

# Calling method
car1.show_details()
car2.show_details()
