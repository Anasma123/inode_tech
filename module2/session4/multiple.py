# ============================================================
# Example: Multiple Inheritance in Python
# Module 2 → Session 4
# ============================================================

# ---------- Parent Class 1 ----------
class Student:
    def study(self):
        # This method belongs to Student class
        # Ee method Student classinte aanu — ivide student padikkunnu
        print("Student is studying...")


# ---------- Parent Class 2 ----------
class Athlete:
    def play(self):
        # This method belongs to Athlete class
        # Ee method Athlete classinte aanu — ivide football kalikkunnu
        print("Athlete is playing football...")


# ---------- Child Class ----------
# Scholar class inherits from both Student and Athlete
# Ee class randu parent classil ninnum inherit cheyyunnu (multiple inheritance)
class Scholar(Student, Athlete):
    def show(self):
        # This method belongs only to Scholar class
        # Ee method Scholar classinte thante aanu — combined role explain cheyyunnu
        print("Scholar is both a student and an athlete!")


# ---------- Object Creation ----------
# Create an object of Scholar class
# Scholar object create cheyyumbol ith Student + Athlete randinte methods inherit cheyyum
s = Scholar()

# ---------- Method Calls ----------
s.show()     # Calls method from Scholar class
# Ithu child classil ninnulla method aanu, scholarinte full role display cheyyum

s.study()    # Inherited from Student class
# Ithu parent class (Student) ninnulla method aanu, student study cheyyunnu

s.play()     # Inherited from Athlete class
# Ithu Athlete classil ninnulla method aanu, athlete football kalikkunnu

