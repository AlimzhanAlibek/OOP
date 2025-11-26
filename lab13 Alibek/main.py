import math_utils
import string_utils
from math_utils import add, divide
from string_utils import capitalize_words
def main():
    print("Математические операции:")
    print(f"Сложение 5 + 3 = {math_utils.add(5, 3)}")
    print(f"Разделение 10 / 2 = {divide(10, 2)}")

    print("\nСтроковые операции:")
    print(f"Капитализация слов: {capitalize_words('hello world')}")
    print(f"Количество букв в 'hello123': {string_utils.count_letters('hello123')}")

if __name__ == "__main__":
    main()
