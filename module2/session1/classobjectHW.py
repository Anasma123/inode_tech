# Homework: Book Information System

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def book_details(self):
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("------------------------")

# Creating Book objects
book1 = Book("Python Basics", "Guido van Rossum", 450)
book2 = Book("Learning Django", "Adrian Holovaty", 600)
book3 = Book("AI for Beginners", "Andrew Ng", 550)

# Calling method
book1.book_details()
book2.book_details()
book3.book_details()
