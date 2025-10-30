class LibraryBook:
    library_name = "Central Library"   # class variable (common)

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("Library:", LibraryBook.library_name)
        print("------------------------")

# creating objects
b1 = LibraryBook("Python Basics", "Guido van Rossum")
b2 = LibraryBook("Django for Web", "Adrian Holovaty")
b3 = LibraryBook("AI Essentials", "Andrew Ng")

# displaying info
b1.display()
b2.display()
b3.display()
