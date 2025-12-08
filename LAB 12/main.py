from classes.shapes import Circle, Rectangle
from classes.employee import Manager, Developer
from classes.library import Book, Magazine

print("=== Shapes ===")
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"Area: {shape.area():.2f}, Perimeter: {shape.perimeter():.2f}")

print("\n=== Employees ===")
employees = [Manager("Alice", 5000, 1500), Developer("Bob", 50, 160)]
for emp in employees:
    print(f"{emp.name}'s salary: {emp.calculate_salary()}")

print("\n=== Library Items ===")
items = [Book("Python 101", "John Doe"), Magazine("Tech Today", 42)]
for item in items:
    item.info()
