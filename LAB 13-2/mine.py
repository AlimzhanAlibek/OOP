import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from shapes.circle import Circle
from shapes.rectangle import Rectangle

def main():

    circle = Circle(5)
    rectangle = Rectangle(4, 6)


    print(f"Площадь круга с радиусом 5: {circle.area()}")
    print(f"Площадь прямоугольника 4x6: {rectangle.area()}")

if __name__ == "__main__":
    main()