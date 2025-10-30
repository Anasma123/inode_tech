class LibraryBook:
    library_name = "Central Library"   # class variable

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("\nBook Title:", self.title)
        print("Author:", self.author)
        print("Library:", LibraryBook.library_name)
        print("-----------------------------")


# ---------- User Input Section ----------
n = int(input("Enter number of books: "))
books = []

for i in range(n):
    print(f"\nEnter details for Book {i+1}:")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    b = LibraryBook(title, author)
    books.append(b)

# ---------- Display Books ----------
for b in books:
    b.display()
