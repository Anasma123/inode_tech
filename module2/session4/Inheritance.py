# ============================================================
# Example: Single Inheritance in Python
# Module 2 → Session 4: Inheritance
# ============================================================

# ---------- Parent Class ----------
class Person:
    def __init__(self, name):
        # Constructor – object create cheyyumbol run aakum
        # self.name → objectinte name attribute store cheyyunnu
        self.name = name

    def show_name(self):
        # Ee function personinte peru display cheyyum
        print("Name:", self.name)


# ---------- Child Class ----------
class Student(Person):  
    # Student class inherits all features of Person class
    # Meaning – Student can use Personinte methods and variables

    def __init__(self, name, course):
        # super() → parent classinte constructor call cheyyan use cheyyunnu
        super().__init__(name)
        # ivide super().__init__(name) → Person classilulla __init__ call cheyyum

        # Extra property course add cheyyunnu child classil
        self.course = course

    def show_course(self):
        # Ee function studentinte course display cheyyum
        print("Course:", self.course)


# ---------- Object Creation ----------
s1 = Student("Anas", "MCA")
# s1 enna object Student classil ninn create cheyyunnu
# Student inherit cheythath kond Personilulla methodum use cheyyam

# ---------- Function Calls ----------
s1.show_name()     # Parent classil ninnulla method call cheyyunnu
s1.show_course()   # Child classilulla method call cheyyunnu
