# ================================================================
# 💡 Module 2 - Session 5
# Topic: Method Overriding, super(), and Polymorphism
# ================================================================

# Parent class
class Vehicle:
    def __init__(self, brand, wheels):
        # brand and wheels are instance variables
        self.brand = brand
        self.wheels = wheels

    def start(self):
        # Generic start message for all vehicles
        print(f"\n{self.brand} vehicle is starting...")

    def show_details(self):
        # Display basic info of vehicle
        print(f"Brand: {self.brand}")
        print(f"Number of Wheels: {self.wheels}")


# --------------------------------------------------------------
# Child Class 1 → Car (Overriding + super())
# --------------------------------------------------------------
class Car(Vehicle):
    def __init__(self, brand, wheels, model, mileage):
        # Call parent constructor using super()
        super().__init__(brand, wheels)
        self.model = model
        self.mileage = mileage

    # Method overriding (same name, different behavior)
    def start(self):
        # Parent class start() also call cheyyunnu (super() use cheythu)
        super().start()
        print(f"{self.model} car engine started successfully 🚗")

    def show_details(self):
        # Extend parent show_details() with extra data
        super().show_details()
        print(f"Model: {self.model}")
        print(f"Mileage: {self.mileage} km/l")


# --------------------------------------------------------------
# Child Class 2 → Bike (Another overriding example)
# --------------------------------------------------------------
class Bike(Vehicle):
    def __init__(self, brand, wheels, type_bike, mileage):
        # Call parent init
        super().__init__(brand, wheels)
        self.type_bike = type_bike
        self.mileage = mileage

    def start(self):
        # Completely overriding parent method
        print(f"\n{self.brand} {self.type_bike} bike started with smooth sound 🏍️")

    def show_details(self):
        super().show_details()
        print(f"Bike Type: {self.type_bike}")
        print(f"Mileage: {self.mileage} km/l")


# --------------------------------------------------------------
# Function demonstrating Polymorphism
# --------------------------------------------------------------
def vehicle_start_demo(vehicle):
    # Function works with any class having .start()
    # ithil parent, child randinum work cheyyum — same method name aanu.
    vehicle.start()
    vehicle.show_details()


# --------------------------------------------------------------
# User Input Section
# --------------------------------------------------------------
print("=== VEHICLE MANAGEMENT SYSTEM ===")
print("1. Car\n2. Bike")
choice = int(input("Enter your choice (1/2): "))

brand = input("Enter brand name: ")
wheels = int(input("Enter number of wheels: "))

if choice == 1:
    model = input("Enter car model: ")
    mileage = float(input("Enter car mileage (km/l): "))
    obj = Car(brand, wheels, model, mileage)

elif choice == 2:
    type_bike = input("Enter bike type (e.g., Sports, Cruiser): ")
    mileage = float(input("Enter bike mileage (km/l): "))
    obj = Bike(brand, wheels, type_bike, mileage)

else:
    print("Invalid choice!")
    exit()

# --------------------------------------------------------------
# Demonstrating Polymorphism
# --------------------------------------------------------------
print("\n--- Vehicle Details and Behavior ---")
vehicle_start_demo(obj)
