# ============================================================
# Example: Method Overriding (Polymorphism Example)
# ============================================================

class Employee:
    # Parent class — general employee role define cheyyunnu
    def role(self):
        print("General Employee")   # Basic role of an employee


class Manager(Employee):
    # Child class — parentinte same method vechu redefine cheyyunnu (override)
    def role(self):
        print("Manager of the team")   # Overridden version of 'role'


# ---------- Object Creation ----------
emp1 = Employee()   # Parent class object
emp2 = Manager()    # Child class object

# ---------- Method Calls ----------
emp1.role()   # Ee call parent classile methodine vilikkum
emp2.role()   # Ee call child classile methodine vilikkum (override cheythath)



# Child classil same method ezhuthumbol,
# ath parent classinte methodine override cheyyum (replace cheyyum)
# pakshe parentinte method still access cheyyan super() use cheyyam.
