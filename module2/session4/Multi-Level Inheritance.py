# ============================================================
# Example: Multi-Level Inheritance in Python
# Module 2 → Session 4: Inheritance
# ============================================================

# ---------- Base Class ----------
class Person:
    def __init__(self, name):
        # This constructor initializes the common attribute 'name'
        # Ithu oru constructor aanu, name ennoru common attribute initialize cheyyunnu
        self.name = name


# ---------- Intermediate Class ----------
class Employee(Person):
    def __init__(self, name, emp_id):
        # Calls the constructor of the parent class (Person)
        # super() use cheythu parent classilulla constructor call cheyyunnu
        super().__init__(name)

        # Adds a new attribute specific to Employee
        # Ithu Employee classinu vendi oru puthiya attribute aanu (emp_id)
        self.emp_id = emp_id


# ---------- Derived Class ----------
class Manager(Employee):
    def __init__(self, name, emp_id, department):
        # Calls the constructor of the parent class (Employee)
        # Ithu Employee classinte constructor ne call cheyyunnu super() vazhi
        super().__init__(name, emp_id)

        # Adds its own attribute specific to Manager
        # Manager classinu vendi thante thante attribute aanu department
        self.department = department

    def show_info(self):
        # Displays all details from all inheritance levels
        # Parent classil ninnulla ella attribute um ivide print cheyyunnu
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Department:", self.department)


# ---------- Object Creation ----------
m1 = Manager("Anas", "E101", "HR")
# Oru Manager object create cheyyunnu
# Constructor chain run aavum: Person → Employee → Manager

# ---------- Method Call ----------
m1.show_info()
# Ee method parentil ninnulla name, emp_id, childil ninnulla department okke display cheyyum
