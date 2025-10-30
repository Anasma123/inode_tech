class Car:
    def __init__(self, model):
        self.model = model

    def show_model(self):
        print("Car model:", self.model)


# ---------- User Input ----------
model_name = input("Enter the car model name: ")

# Create one object
car1 = Car(model_name)

# Assign another variable to the same object
car2 = car1

print("\nBefore changing model:")
car1.show_model()
car2.show_model()

# ---------- Update through car2 ----------
new_model = input("\nEnter new model name to update through car2: ")
car2.model = new_model

print("\nAfter changing through car2:")
car1.show_model()
car2.show_model()

# ---------- Optional: Verify memory address ----------
print("\nMemory address of car1:", id(car1))
print("Memory address of car2:", id(car2))
