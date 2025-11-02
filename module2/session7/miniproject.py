# ==============================================
# 📘 Mini Project: Student Record Management System
# ==============================================
# Features:
# 1️⃣ Add new student records
# 2️⃣ View all stored students
# 3️⃣ Exit safely
# Uses file handling with append & read modes
# ==============================================


# ---------- Function to Add Student ----------
def add_student():
    # User input edukkunnu student details
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    grade = input("Enter Grade: ")

    # File open cheyyunnu append mode-il ('a')
    # 'with open' → automatic close cheyyum even if error vannalum
    with open("students.txt", "a") as f:
        # Data file-il comma-separated aayi ezhuthunnu
        # Oru student oru line aayi store cheyyum
        f.write(f"{name},{age},{grade}\n")

    print("✅ Student record saved successfully.")



# ---------- Function to View Students ----------
def view_students():
    print("\n--- All Student Records ---")

    # Try block use cheythu file illa scenario handle cheyyan
    try:
        with open("students.txt", "r") as f:
            # Oru line-onnum illenkil empty check
            lines = f.readlines()
            if not lines:
                print("No records found.")
                return

            # Each line loop cheyyunnu
            for line in lines:
                # strip() → remove newline
                # split(",") → divide values by comma
                n, a, g = line.strip().split(",")
                print(f"Name: {n} | Age: {a} | Grade: {g}")

    except FileNotFoundError:
        print("⚠️ File not found! Please add a record first.")



# ---------- Main Menu ----------
while True:
    print("\n==============================")
    print(" Student Record Management ")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    # User choice input
    try:
        ch = int(input("Enter your choice (1-3): "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    # Menu options handle cheyyunnu
    if ch == 1:
        add_student()
    elif ch == 2:
        view_students()
    elif ch == 3:
        print("Exiting program... 👋")
        break
    else:
        print("Please enter a valid choice (1-3).")
