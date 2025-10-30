class Student:
    # class variable (shared)
    school = "ABC Public School"

    def __init__(self, name, roll):
        # instance variables (unique)
        self.name = name
        self.roll = roll

    def show(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("School:", Student.school)
        print("-------------------------")

# creating objects
s1 = Student("Anas", 101)
s2 = Student("Fathima", 102)

# displaying info
s1.show()
s2.show()

# change class variable
Student.school = "XYZ Model School"


s1.show()
s2.show()
