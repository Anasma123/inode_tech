# =====================================================
# 🧾 Complete File Handling Project: Student Management
# =====================================================
# Features:
# 1️⃣ Add New Students
# 2️⃣ View All Students
# 3️⃣ Search Student by Name
# 4️⃣ Delete Student Record
# 5️⃣ Exit Program
# =====================================================


# ---------- Function to Add Student ----------
def add_student():
    # User input edukkunnu
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    grade = input("Enter Grade: ")

    # File open cheyyunnu append mode-il ('a')
    # 'with open' use cheythal auto close aakum even if error vannalum
    with open("students.txt", "a") as f:
        # Oru line-il name, age, grade comma-separated aayi ezhuthunnu
        f.write(f"{name},{age},{grade}\n")

    print("✅ Student record added successfully.")



# ---------- Function to View All Students ----------
def view_students():
    print("\n--- All Student Records ---")

    try:
        # File open cheyyunnu read mode-il ('r')
        with open("students.txt", "r") as f:
            lines = f.readlines()  # File-il ulla lines list form-il kittum
            if not lines:
                print("No records found.")
                return

            # Oru line each student data aayi display cheyyunnu
            for line in lines:
                # strip() newline remove cheyyum, split(',') comma basis-il divide cheyyum
                n, a, g = line.strip().split(",")
                print(f"Name: {n} | Age: {a} | Grade: {g}")

    except FileNotFoundError:
        print("⚠️ No file found. Please add a record first.")



# ---------- Function to Search a Student ----------
def search_student():
    search_name = input("Enter name to search: ").strip()

    found = False
    try:
        # File open cheyyunnu read mode-il
        with open("students.txt", "r") as f:
            for line in f:
                # Line clean cheythu split cheyyunnu
                n, a, g = line.strip().split(",")
                if n.lower() == search_name.lower():  # case insensitive compare
                    print(f"\n✅ Record Found:\nName: {n} | Age: {a} | Grade: {g}")
                    found = True
                    break

        if not found:
            print("❌ No matching student found.")

    except FileNotFoundError:
        print("⚠️ File not found! Please add a record first.")



# ---------- Function to Delete a Student Record ----------
def delete_student():
    delete_name = input("Enter name to delete: ").strip()
    found = False

    try:
        # Read all existing lines
        with open("students.txt", "r") as f:
            lines = f.readlines()

        # Puthiya list create cheyyunnu keep only undeleted data
        with open("students.txt", "w") as f:
            for line in lines:
                n, a, g = line.strip().split(",")
                # If name match aakathenkil puthiya file-il retain cheyyum
                if n.lower() != delete_name.lower():
                    f.write(line)
                else:
                    found = True

        if found:
            print("✅ Student record deleted successfully.")
        else:
            print("❌ No student found with that name.")

    except FileNotFoundError:
        print("⚠️ File not found! Please add a record first.")



# ---------- Function to Initialize File ----------
def create_file_if_not_exist():
    # Try opening file read mode-il
    try:
        open("students.txt", "r").close()
    except FileNotFoundError:
        # File illeenkil create cheyyunnu empty aayi
        with open("students.txt", "w") as f:
            pass



# ---------- Main Menu ----------
create_file_if_not_exist()

while True:
    print("\n=====================================")
    print("      📚 Student File Management      ")
    print("=====================================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Name")
    print("4. Delete Student Record")
    print("5. Exit Program")
    print("=====================================")

    # User choice input edukkunnu
    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    # User choice check cheyyunnu
    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        print("👋 Exiting the program. Have a nice day!")
        break
    else:
        print("⚠️ Invalid choice. Please enter between 1–5.")
