# ==============================================================
#  MODULE 2 – SESSION 1
#  PROJECT: Student Performance Management System using OOP
# ==============================================================

# This project demonstrates:
# 👉 Class creation
# 👉 Objects
# 👉 Constructors (__init__)
# 👉 self keyword
# 👉 Methods
# 👉 Multiple objects
# 👉 Encapsulation
# 👉 Practical real-world implementation

# ==============================================================

# Step 1️⃣: Define a Class called Student
class Student:  # 'Student' class represents one student record
    """
    A class to represent a student's academic performance.
    """

    # Step 2️⃣: Constructor (__init__) is called automatically when we create an object.
    # It initializes variables like name, reg_no, marks, total, average, and grade.
    def __init__(self, name, reg_no, marks):
        self.name = name          # 'self.name' → stores the student's name (instance variable)
        self.reg_no = reg_no      # 'self.reg_no' → stores registration number
        self.marks = marks        # 'self.marks' → stores marks as a list [mark1, mark2, mark3]
        self.total = sum(marks)   # Calculates total by summing all marks using built-in 'sum()'
        self.average = self.total / len(marks)  # Average = total ÷ number of subjects
        self.grade = self.calculate_grade()     # Calls another method to find grade

    # Step 3️⃣: Method to calculate grade based on average marks
    def calculate_grade(self):
        # If-elif ladder to decide grade
        if self.average >= 90:
            return "A+"
        elif self.average >= 80:
            return "A"
        elif self.average >= 70:
            return "B+"
        elif self.average >= 60:
            return "B"
        elif self.average >= 50:
            return "C"
        else:
            return "Fail"

    # Step 4️⃣: Method to display the details of the student
    def display(self):
        # f-string formatting used for clear and clean printing
        print(f"\n📘 Student Name  : {self.name}")
        print(f"🆔 Register No.  : {self.reg_no}")
        print(f"📊 Marks         : {self.marks}")
        print(f"🧮 Total Marks   : {self.total}")
        print(f"📈 Average Marks : {self.average:.2f}")  # .2f = round to 2 decimal points
        print(f"🎓 Grade         : {self.grade}")
        print("-" * 50)  # prints a separator line


# ==============================================================
# Step 5️⃣: Create another class called StudentManager
# This class manages multiple Student objects together.
# ==============================================================

class StudentManager:
    def __init__(self):
        self.students = []  # Empty list to store all Student objects

    # Step 6️⃣: Method to add new student record
    def add_student(self):
        # Take input from user for name and register number
        name = input("\nEnter Student Name: ")
        reg_no = input("Enter Register Number: ")

        marks = []  # Empty list to store marks
        for i in range(3):  # Loop runs 3 times for 3 subjects
            while True:  # Keep asking until valid input given
                try:
                    mark = float(input(f"Enter Mark {i+1}: "))  # Get each mark
                    if 0 <= mark <= 100:  # Validate mark between 0 and 100
                        marks.append(mark)
                        break  # exit inner loop if valid mark
                    else:
                        print("❌ Marks should be between 0 and 100.")
                except ValueError:  # Handles invalid (non-numeric) input
                    print("❌ Invalid input. Please enter a number.")

        # Create a Student object using user inputs
        student = Student(name, reg_no, marks)
        # Append this object to the students list
        self.students.append(student)
        print(f"\n✅ Record added successfully for {name}!")

    # Step 7️⃣: Display all student records
    def display_all(self):
        # Check if any student exists
        if not self.students:
            print("\n⚠️ No student records found!")
            return

        print("\n===== STUDENT PERFORMANCE REPORT =====")
        for student in self.students:
            student.display()  # Call display() method from each student object

    # Step 8️⃣: Find and show the top performer
    def show_topper(self):
        if not self.students:
            print("\n⚠️ No student records found!")
            return

        # max() with lambda to compare average of each student
        topper = max(self.students, key=lambda s: s.average)
        print("\n🏆 TOP PERFORMER OF THE CLASS 🏆")
        topper.display()

    # Step 9️⃣: Find and show lowest performer
    def show_lowest(self):
        if not self.students:
            print("\n⚠️ No student records found!")
            return

        # min() with lambda to find lowest average
        lowest = min(self.students, key=lambda s: s.average)
        print("\n📉 LOWEST PERFORMANCE STUDENT 📉")
        lowest.display()

    # Step 🔟: Show class summary (overall average, total students)
    def show_summary(self):
        if not self.students:
            print("\n⚠️ No student records found!")
            return

        total_students = len(self.students)  # Count of students
        overall_avg = sum(s.average for s in self.students) / total_students
        print("\n📊 CLASS SUMMARY 📊")
        print(f"Total Students : {total_students}")
        print(f"Overall Average: {overall_avg:.2f}")
        print("-" * 50)


# ==============================================================
# Step 1️⃣1️⃣: Main Function → Controls the entire program flow
# ==============================================================

def main():
    print("🎓 Welcome to Student Performance Management System 🎓")

    # Create object of StudentManager to manage all data
    manager = StudentManager()

    # Infinite loop to keep menu running until user exits
    while True:
        print("\n=========== MENU ===========")
        print("1️⃣ Add New Student")
        print("2️⃣ Display All Records")
        print("3️⃣ Show Top Performer")
        print("4️⃣ Show Lowest Performer")
        print("5️⃣ Show Class Summary")
        print("6️⃣ Exit")
        choice = input("Enter your choice (1-6): ")

        # Menu Options Control
        if choice == '1':
            manager.add_student()  # Call function to add student
        elif choice == '2':
            manager.display_all()  # Show all students
        elif choice == '3':
            manager.show_topper()  # Show topper student
        elif choice == '4':
            manager.show_lowest()  # Show lowest performer
        elif choice == '5':
            manager.show_summary()  # Show summary report
        elif choice == '6':
            print("\n👋 Exiting program. Goodbye!")
            break  # Exit the loop → end program
        else:
            print("❌ Invalid choice! Please enter 1–6.")


# ==============================================================
# Step 1️⃣2️⃣: Entry Point of the Program
# ==============================================================
# This ensures that 'main()' runs only when the file is executed directly.

if __name__ == "__main__":
    main()  # Start the program
