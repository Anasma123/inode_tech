class Car:
    def __init__(self, model):
        self.model = model

    def show_model(self):
        print("Car model:", self.model)


# Creating one object
car1 = Car("BMW")

# Assigning another variable to same object
car2 = car1   # both refer to the same memory location

print("Before changing:")
car1.show_model()
car2.show_model()

# Changing model using car2
car2.model = "Audi"

print("\nAfter changing through car2:")
car1.show_model()
car2.show_model()
