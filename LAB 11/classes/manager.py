class LibrarianMI:
    def manage_books(self):
        print("Librarian manages the books.")


class Cataloger:
    def manage_books(self):
        print("Cataloger categorizes the books.")


class LibraryManager(LibrarianMI, Cataloger):
    def manage_books(self):
        super().manage_books()
        print("Library Manager oversees all operations.")
