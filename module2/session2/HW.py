# ==============================================================
# CLASS: LibraryBook
# Demonstrates CLASS and INSTANCE variables
# ==============================================================

class LibraryBook:
    library_name = "Central Library"   # Class variable → common for all books

    # Constructor (__init__) — runs automatically when object is created
    def __init__(self, title, author):
        self.title = title     # Instance variable → stores book title
        self.author = author   # Instance variable → stores author name

    # Method to display details of each book
    def display(self):
        print("Book Title:", self.title)               # Access instance variable
        print("Author:", self.author)                  # Access instance variable
        print("Library:", LibraryBook.library_name)    # Access class variable using ClassName
        print("------------------------")


# ==============================================================
# OBJECT CREATION
# ==============================================================

# Each object represents a unique book (different title & author)
b1 = LibraryBook("Python Basics", "Guido van Rossum")
b2 = LibraryBook("Django for Web", "Adrian Holovaty")
b3 = LibraryBook("AI Essentials", "Andrew Ng")

# ==============================================================
# DISPLAY INFORMATION
# ==============================================================

# Call display() method for each book
b1.display()
b2.display()
b3.display()
