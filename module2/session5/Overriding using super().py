# =====================================================
# Example: Method Overriding using super()
# =====================================================

class Vehicle:
    # Parent class - general vehicle behavior define cheyyunnu
    def start(self):
        print("Starting vehicle...")   # Parent method - basic start action


class Car(Vehicle):
    # Child class - parent classil ninn inherit cheythu
    def start(self):
        super().start()   # 👈 parent classinte start() methodine call cheyyunnu
        print("Car engine started!")   # Child classinte own message


# ---------- Object Creation ----------
c1 = Car()   # Car object create cheyyunnu

# ---------- Method Call ----------
c1.start()   # Car classinte start() call cheyyumbo,
             # adyam super() parentinte start() call cheyyum,
             # pinne childinte start() execute aavum.


