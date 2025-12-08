class Library:
    def info(self):
        print("This is a library.")


class Book(Library):
    def info(self):
        print("This is a book stored in the library.")


class Librarian(Library):
    def info(self):
        print("This is a librarian who works in the library.")
