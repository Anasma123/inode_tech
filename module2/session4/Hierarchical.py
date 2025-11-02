# ============================================================
# Example: Hierarchical Inheritance in Python
# Module 2 → Session 4: Inheritance
# ============================================================

class Person:
    def __init__(self, name):
        # Constructor – initializes the common attribute 'name'
        # Ee constructor name enna common attribute initialize cheyyunnu
        self.name = name

    def show_name(self):
        # Displays the name of the person
        # Ee function personinte peru print cheyyum
        print("Name:", self.name)


# ---------- Child Class 1 ----------
class Student(Person):
    def show_role(self):
        # Displays the role as Student
        # Ee method parayunnu ee name ullavan oru student aanu
        print(self.name, "is a Student")


# ---------- Child Class 2 ----------
class Teacher(Person):
    def show_role(self):
        # Displays the role as Teacher
        # Ee method parayunnu ee name ullavan oru teacher aanu
        print(self.name, "is a Teacher")


# ---------- Object Creation ----------
s1 = Student("Anas")
# Oru Student object create cheyyunnu, parent class Person ninn inherit cheythu

t1 = Teacher("Fathima")
# Oru Teacher object create cheyyunnu, ithum Person class ninn inherit cheythu

# ---------- Method Calls ----------
s1.show_name()    # From parent class
# Ee call Person classil ninnulla show_name() method aakum

s1.show_role()    # From Student class
# Ee call Student classil define cheytha show_role() method aanu

t1.show_name()    # From parent class
# Teacher object parent classinte show_name() use cheyyunnu

t1.show_role()    # From Teacher class
# Teacher classinte thante method aanu ee show_role()
