# ============================================================
# Example: Object Reference Behavior (User Input Version)
# Module 2 → Session 3: Names and Object References
# ============================================================

class Car:
    def __init__(self, model):
        # Constructor aanu – object create cheyyumbol ee method auto run aavum
        # self.model → ivide objectinte model name store cheyyunnu
        self.model = model

    def show_model(self):
        # Ee function carinte model name print cheyyum
        print("Car model:", self.model)


# ---------- User Input Section ----------
model_name = input("Enter the car model name: ")
# User ninnu model name edukkunnu

# Oru object create cheyyunnu Car classil ninn
car1 = Car(model_name)
# car1 enna variable ippo ee object ne refer cheyyunnu (memoryil store aayi)

# car2 nu car1 assign cheyyunnu – puthiya object alla
car2 = car1
# Ippol car1 um car2 um oru object ne point cheyyunnu

print("\nBefore changing model:")
car1.show_model()
car2.show_model()
# Randum same model print cheyyum karanam oru object aanu


# ---------- Update through car2 ----------
new_model = input("\nEnter new model name to update through car2: ")
car2.model = new_model
# car2 vazhi model maattiyaal, car1 ilum ath change aavum
# Reason: randum oru memory location aanu share cheyyunnath

print("\nAfter changing through car2:")
car1.show_model()
car2.show_model()


# ---------- Optional: Verify memory address ----------
print("\nMemory address of car1:", id(car1))
print("Memory address of car2:", id(car2))
# id() function objectinte memory address kaanikkum
# Ee randum same aanel randum oru object ne refer cheyyunnu enn proof
