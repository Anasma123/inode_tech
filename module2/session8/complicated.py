# ---------------------------------------------
# Step 1: Import re module for Regular Expressions
# ---------------------------------------------
# re module text pattern validate cheyyan upayogikkunnu (name, email, phone)
import re


# ---------------------------------------------
# Step 2: Generator function for Auto ID
# ---------------------------------------------
def id_generator():
    num = 1  # starting number
    while True:  # infinite loop (new ID on each next() call)
        yield f"USR{num:03d}"  # generate ID like USR001, USR002...
        num += 1  # increment number for next user


# generator object create cheyyunnu
gen = id_generator()


# ---------------------------------------------
# Step 3: Function to Add a New User
# ---------------------------------------------
def add_user():
    with open("users.txt", "a") as f:  # open file in append mode
        while True:
            print("\n=== Add New User ===")

            # take inputs
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            phone = input("Enter Phone Number: ")

            # validate name (only alphabets)
            if not re.match(r"^[A-Za-z ]+$", name):
                print("❌ Invalid Name! Use only letters and spaces.")
                continue

            # validate email
            if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
                print("❌ Invalid Email Format!")
                continue

            # validate phone (exact 10 digits)
            if not re.match(r"^\d{10}$", phone):
                print("❌ Invalid Phone! Must be 10 digits.")
                continue

            # generate new ID using generator
            uid = next(gen)
            print(f"✅ User ID generated: {uid}")

            # save user record in file
            f.write(f"{uid},{name},{email},{phone}\n")
            print("✅ User Saved Successfully!")

            # ask user if they want to continue
            more = input("Add another user? (y/n): ").lower()
            if more != 'y':
                break


# ---------------------------------------------
# Step 4: Function to View All Users
# ---------------------------------------------
def view_users():
    try:
        with open("users.txt", "r") as f:
            data = f.readlines()

            if not data:
                print("⚠️ No users found!")
                return

            print("\n=== All Registered Users ===")
            for line in data:
                uid, name, email, phone = line.strip().split(",")
                print(f"ID: {uid} | Name: {name} | Email: {email} | Phone: {phone}")
    except FileNotFoundError:
        print("❌ No user data file found! Please add users first.")


# ---------------------------------------------
# Step 5: Function to Delete a User by ID
# ---------------------------------------------
def delete_user():
    try:
        with open("users.txt", "r") as f:
            users = f.readlines()

        if not users:
            print("⚠️ No users to delete!")
            return

        del_id = input("Enter User ID to delete (e.g., USR001): ")

        found = False
        with open("users.txt", "w") as f:
            for line in users:
                if line.startswith(del_id + ","):
                    found = True
                    print(f"✅ User {del_id} deleted successfully!")
                    continue
                f.write(line)

        if not found:
            print("❌ User ID not found!")
    except FileNotFoundError:
        print("❌ File not found! Add some users first.")


# ---------------------------------------------
# Step 6: Function to Search User by Name or Email
# ---------------------------------------------
def search_user():
    try:
        keyword = input("Enter name or email to search: ").lower()
        found = False
        with open("users.txt", "r") as f:
            print("\n=== Search Results ===")
            for line in f:
                if keyword in line.lower():
                    print(line.strip())
                    found = True
        if not found:
            print("❌ No matching records found!")
    except FileNotFoundError:
        print("❌ User file not found!")


# ---------------------------------------------
# Step 7: Main Menu (Program Control)
# ---------------------------------------------
while True:
    print("\n========= USER MANAGEMENT SYSTEM =========")
    print("1. Add User")
    print("2. View Users")
    print("3. Search User")
    print("4. Delete User")
    print("5. Exit")
    print("==========================================")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_user()
    elif choice == '2':
        view_users()
    elif choice == '3':
        search_user()
    elif choice == '4':
        delete_user()
    elif choice == '5':
        print("👋 Exiting program. Thank you!")
        break
    else:
        print("❌ Invalid choice! Try again.")
