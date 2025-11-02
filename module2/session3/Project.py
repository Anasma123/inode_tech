# ============================================================
# Example: Object Reference Behavior in Python
# Module 2 → Session 3: Names, Objects, and References
# ============================================================

class Car:
    # Constructor method - initializes the 'model' attribute when object is created
    def __init__(self, model):
        self.model = model
        #  ithu constructor aanu. ivide object create cheyyumbol model name assign cheyyum.

    def show_model(self):
        # Method to display car model
        print("Car model:", self.model)
        #  ivide carinte model name print cheyyum.


# Creating one object of Car class
car1 = Car("BMW")   # car1 points to a Car object with model 'BMW'
#  car1 oru object aanu, ithu memoryil store cheythittundu.

# Assigning another variable to same object
car2 = car1   # both refer to same memory location
#  car2 nu car1 ne equal cheythath kond, randum oru object ne refer cheyyunnu.

print("Before changing:")
car1.show_model()
car2.show_model()

# Changing the model name using car2 reference
car2.model = "Audi"
#  car2 vazhi model value maattiyaal, car1 ilum change aavum — randum same object aanu.

print("\nAfter changing through car2:")
car1.show_model()
car2.show_model()
