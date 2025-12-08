class LowPriceError(Exception):
    """Выбрасывается, если цена книги меньше 1500 тенге."""
    pass

try:
    price = float(input("Введите стоимость книги: "))
    if price < 1500:
        raise LowPriceError("Слишком низкая цена! Книгу нельзя добавить.")
    print("Цена принята.")
except ValueError:
    print("Ошибка: нужно вводить числовое значение.")
except LowPriceError as error:
    print("Исключение пользователя:", error)
