# ==============================================================
# CLASS: LibraryBook
# Demonstrates CLASS and INSTANCE variables with user input
# ==============================================================

class LibraryBook:
    library_name = "Central Library"   # Class variable → common for all books

    # Constructor — initializes each book's title and author
    def __init__(self, title, author):
        self.title = title      # Instance variable → book title (unique)
        self.author = author    # Instance variable → author name (unique)

    # Method to display book details
    def display(self):
        print("\nBook Title:", self.title)
        print("Author:", self.author)
        print("Library:", LibraryBook.library_name)   # Access class variable
        print("-----------------------------")


# ==============================================================
# USER INPUT SECTION
# ==============================================================

# Ask the user how many books to add
n = int(input("Enter number of books: "))
books = []     # Empty list to store multiple LibraryBook objects

# Loop runs 'n' times to take multiple book details
for i in range(n):
    print(f"\nEnter details for Book {i+1}:")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    b = LibraryBook(title, author)   # Create LibraryBook object
    books.append(b)                  # Add it to the list

# ==============================================================
# DISPLAY SECTION
# ==============================================================

# Display all book details using loop
for b in books:
    b.display()



'''
print(f"\nEnter details for Book {i+1}:")
# Printing which book details user is entering
# \n → adds a new blank line before text for better readability
# f"..." → f-string allows inserting variables directly inside the string
# {i+1} → since 'i' starts from 0, adding 1 makes it Book 1, Book 2, etc.
'''
