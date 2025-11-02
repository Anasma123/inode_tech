# ===============================================================
# 💡 Example: Encapsulation using Getter and Setter
# ===============================================================

class Student:
    def __init__(self, name, marks):
        # __name and __marks are private variables
        # means ivay classinte ullil mathram access cheyyan pattum
        self.__name = name
        self.__marks = marks

    # ---------- Setter Function ----------
    # this safely updates the private variable
    def set_marks(self, marks):
        # validation: marks negative aano enn check cheyyunnu
        if marks >= 0:
            self.__marks = marks
            print("✅ Marks updated successfully!")
        else:
            print("❌ Invalid marks entered! Marks cannot be negative.")

    # ---------- Getter Function ----------
    # safely returns the private value without direct access
    def get_marks(self):
        return self.__marks

    # ---------- Display Function ----------
    def show(self):
        print("\n--- Student Details ---")
        print("Name:", self.__name)
        print("Marks:", self.__marks)


# ---------- Object Creation ----------
s = Student("Anas", 90)   # valid data pass cheythu
s.show()                  # initial details print cheyyunnu

# ---------- Try to Update Marks ----------
s.set_marks(-30)          # ❌ invalid update (will show warning)
s.set_marks(95)           # ✅ valid update

# ---------- Read Marks Safely ----------
print("Updated Marks (using getter):", s.get_marks())
