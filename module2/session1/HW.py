# Program: Create a Book Information System using Classes and Objects in Python

# -------------------------------
# Class Definition
# -------------------------------
# 'Book' class represents a book with its basic details.
# It includes a constructor to initialize book data and a method to display it.

class Book:
    # Constructor: initializes book details (title, author, price)
    def __init__(self, title, author, price):
        self.title = title       # Book title
        self.author = author     # Book author name
        self.price = price       # Book price

    # Method to display book details
    def book_details(self):
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("------------------------")


# -------------------------------
# Object Creation
# -------------------------------
# Creating multiple book objects with different data
book1 = Book("Python Basics", "Guido van Rossum", 450)
book2 = Book("Learning Django", "Adrian Holovaty", 600)
book3 = Book("AI for Beginners", "Andrew Ng", 550)


# -------------------------------
# Displaying Book Information
# -------------------------------
# Calling the 'book_details()' method for each book
book1.book_details()
book2.book_details()
book3.book_details()
