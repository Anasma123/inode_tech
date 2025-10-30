class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Anas")
s2.name = "Rahul"

s2 = s1       # both refer to same object
s3 = Student("Fathima")

print(s1.name)   # Anas
print(s2.name)   # Anas
print(s3.name)   # Fathima

print(s1.name)   # Rahul  (same object updated!)
