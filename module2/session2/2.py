class Student:
    count = 0        # class variable

    def __init__(self, name):
        self.name = name
        Student.count += 1   # increase every time object created

    def show(self):
        print("Student Name:", self.name)

# create objects
s1 = Student("Anas")
s2 = Student("Fathima")
s3 = Student("Rahul")

# display
s1.show()
s2.show()
print("Total Students:", Student.count)
