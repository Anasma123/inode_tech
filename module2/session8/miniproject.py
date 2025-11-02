# ---------------------------------------------
# Step 1: Import re module for Regular Expressions
# ---------------------------------------------
# re module use cheyyunnu text pattern check cheyyan (email, phone, etc.)
import re


# ---------------------------------------------
# Step 2: Create a Generator function for auto user ID
# ---------------------------------------------
def id_generator():
    num = 1  # starting number 1
    while True:  # infinite loop for generating IDs continuously
        yield f"USER{num:03d}"  # 'yield' ith return cheyyum (ex: USER001, USER002)
        num += 1  # number increment cheyyum next ID venam


# Generator object create cheyyunnu
gen = id_generator()


# ---------------------------------------------
# Step 3: Open file to save user details
# ---------------------------------------------
# with open() → automatically close cheyyum
# 'a' mode → append cheyyum, old data delete aakilla
with open("users.txt", "a") as f:

    # infinite loop until user stops manually
    while True:
        # ---------------------------------------------
        # Step 4: Take user inputs
        # ---------------------------------------------
        name = input("Enter name: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")

        # ---------------------------------------------
        # Step 5: Validate each input using Regular Expressions
        # ---------------------------------------------
        # Name → alphabets only
        if not re.match(r"^[a-zA-Z]+$", name):
            print("❌ Invalid name! Use only letters.")
            continue  # re-enter input

        # Email → must follow correct format (username@domain.com)
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            print("❌ Invalid email format!")
            continue

        # Phone → exactly 10 digits
        if not re.match(r"^\d{10}$", phone):
            print("❌ Phone must have 10 digits!")
            continue

        # ---------------------------------------------
        # Step 6: Generate unique user ID from generator
        # ---------------------------------------------
        uid = next(gen)  # next() call cheyyumbol generator ninn next ID varum
        print(f"✅ User ID: {uid}")

        # ---------------------------------------------
        # Step 7: Save user data into file
        # ---------------------------------------------
        f.write(f"{uid},{name},{email},{phone}\n")  # CSV formatil store cheyyunnu
        print("✅ User saved successfully!\n")

        # ---------------------------------------------
        # Step 8: Check if user wants to add more
        # ---------------------------------------------
        more = input("Add another user? (y/n): ").lower()
        if more != 'y':
            break  # loop stop cheyyum


# ---------------------------------------------
# Step 9: Final message
# ---------------------------------------------
print("✅ All data saved in users.txt")
