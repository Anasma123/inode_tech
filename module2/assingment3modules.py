# ---------- Global Namespace ----------
school_name = input("Enter the Global School Name: ")

class Student:
    # Class variable (shared by all objects)
    total_students = 0

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
        Student.total_students += 1

    # Method 1: Show student details using the global variable
    def show_details(self):
        print(f"\nStudent Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"School (Global): {school_name}")

    # Method 2: Redefine school name locally and compare with global
    def redefine_school(self):
        school_name = input(f"\nEnter a local school name for {self.name}: ")
        print(f"{self.name} studies in (Local): {school_name}")
        print(f"Outside (Global) School still: {globals()['school_name']}")

    # Method 3: Show namespaces
    def show_namespaces(self):
        print("\n--- Local Namespace of this Method ---")
        print(locals())          # local variables in this method
        print("\n--- Global Namespace Keys ---")
        print(list(globals().keys())[:10], "...")  # first few global keys


# ---------- Create First Object from User Input ----------
name1 = input("\nEnter first student name: ")
age1 = int(input("Enter age: "))
s1 = Student(name1, age1)

# ---------- Create Second Reference (Same Object) ----------
s2 = s1  # s2 refers to the same object as s1

print("\n--- Before Updating Through s2 ---")
s1.show_details()
s2.show_details()

# ---------- Update Age Through s2 ----------
new_age = int(input("\nEnter new age to update through s2: "))
s2.age = new_age

print("\n--- After Updating Through s2 ---")
s1.show_details()
s2.show_details()

# ---------- Show Object Memory IDs ----------
print("\nMemory ID of s1:", id(s1))
print("Memory ID of s2:", id(s2))

# ---------- Demonstrate Global vs Local Variable ----------
s1.redefine_school()

# ---------- Display Namespaces ----------
s1.show_namespaces()

# ---------- Class Variable Output ----------
print("\nTotal Students Created:", Student.total_students)
