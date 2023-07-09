class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_books(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def showInfo(self):
        print(f"The Library has {self.no_of_books} books.\nThe books are")
        for book in self.books:
            print(book)

    
l1 = Library()
l1.add_books("Harry Potter 1")
l1.add_books("Harry Potter 2")
l1.add_books("Harry Potter 3")
l1.add_books("Harry Potter 4")
l1.add_books("Harry Potter 5")
print(l1.showInfo())

