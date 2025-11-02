# ============================================================
# Example: Polymorphism & Method Overriding using super()
# Module 2 → Session 5
# ============================================================

# ---------- Base Class ----------
class Bird:
    def make_sound(self):
        # This is the general behavior of all birds
        # Ith oru base method aanu, ella birdsinum common aayittulla sound
        print("Some generic bird sound")


# ---------- Derived Class 1 ----------
class Parrot(Bird):
    def make_sound(self):
        # Calls the parent class version first
        # super() use cheythu parentinte method call cheyyunnu
        super().make_sound()
        
        # Then adds its own specific sound
        # Appol parrot thante thante special sound add cheyyum
        print("Parrot says: Hello!")


# ---------- Derived Class 2 ----------
class Crow(Bird):
    def make_sound(self):
        # Call parent method using super()
        # Parent method first run cheyyum
        super().make_sound()

        # Then child class adds its own message
        # Crow thante thante sound add cheyyum
        print("Crow says: Caw Caw!")


# ---------- Function Demonstrating Polymorphism ----------
def sound_test(bird):
    # This function accepts any object that has a make_sound() method
    # Ee function polymorphism kaanikunnu — oru object type aanu, behavior change aavum
    bird.make_sound()


# ---------- Object Creation ----------
b1 = Parrot()  # Parrot object create cheyyunnu
b2 = Crow()    # Crow object create cheyyunnu

# ---------- Function Calls ----------
sound_test(b1)  # Parrot’s overridden method will run
sound_test(b2)  # Crow’s overridden method will run
