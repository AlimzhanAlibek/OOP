from classes.person import Person, Reader
from classes.library import Library, Book, Librarian
from classes.items import Item, BookShelf, Table
from classes.manager import LibrarianMI, Cataloger, LibraryManager

# === Демонстрация работы ===

print("=== Person / Reader ===")
r = Reader("Aibek", 19, "RD102")
r.display_info()

print("\n=== Library Polymorphism ===")
objects = [Library(), Book(), Librarian()]
for obj in objects:
    obj.info()

print("\n=== Item Areas ===")
items = [BookShelf(100, 180), Table(120, 70)]
for obj in items:
    print("Area:", obj.area())

print("\n=== Multiple Inheritance ===")
manager = LibraryManager()
manager.manage_books()
