# ===============================================================
# 💡 Module 2 - Session 6
# Topic: Encapsulation, Data Hiding, Getter & Setter
# ===============================================================

# ---------------------------------------------------------------
# ❌ Part 1: Without Encapsulation (unsafe data)
# ---------------------------------------------------------------
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s = Student("Anas", 90)
print("---- Without Encapsulation ----")
print("Name:", s.name)
print("Marks:", s.marks)

# Direct modification – no validation
s.marks = 150
print("After changing marks (invalid):", s.marks)


# ---------------------------------------------------------------
# ✅ Part 2: With Encapsulation (safe data)
# ---------------------------------------------------------------
class SafeStudent:
    def __init__(self, name, marks):
        self.__name = name         # private variable
        self.__marks = marks       # private variable

    def get_marks(self):
        # safely return marks
        return self.__marks

    def set_marks(self, marks):
        # validation check
        if 0 <= marks <= 100:
            self.__marks = marks
            print("✅ Marks updated successfully!")
        else:
            print("❌ Invalid marks! Enter between 0–100.")

    def show_info(self):
        print("\n---- With Encapsulation ----")
        print("Name:", self.__name)
        print("Marks:", self.__marks)


# ---------- User Input ----------
name = input("\nEnter Student Name: ")
marks = float(input("Enter Student Marks: "))

s1 = SafeStudent(name, marks)
s1.show_info()

new_marks = float(input("\nEnter new marks to update: "))
s1.set_marks(new_marks)
s1.show_info()

# print(s1.__marks)   # ❌ Error: can't access private variable directly
