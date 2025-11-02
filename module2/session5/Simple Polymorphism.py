# ============================================================
# Example: Simple Polymorphism in Python
# Module 2 → Session 5
# ============================================================

# ---------- Class 1 ----------
class Dog:
    def speak(self):
        # This method defines the Dog's behavior
        # Ee method doginte sound represent cheyyunnu
        return "Bark"


# ---------- Class 2 ----------
class Cat:
    def speak(self):
        # This method defines the Cat's behavior
        # Ee method catinte sound represent cheyyunnu
        return "Meow"


# ---------- Polymorphism in Action ----------
# Both classes have the same method name (speak),
# but each behaves differently.
# Randum same method aanu (speak), pakshe behavior vereyaanu

for animal in (Dog(), Cat()):
    # Loop creates objects of both Dog and Cat
    # Ee loop randu object create cheyyunnu
    print(animal.speak())
    # Method call cheyyumbol appropriate version run cheyyum
    # Dog object aanenkil 'Bark', Cat aanenkil 'Meow'
