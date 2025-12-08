try:
    with open(r"C:\Users\Аяжан\OneDrive\Desktop\Әлібек Сабак\LAB 10\книги.txt", "r", encoding="utf-8") as file:
        prices = []
        for line in file:
            title, price = line.strip().split(", ")
            price_value = float(price)
            prices.append(price_value)
            print(f"{title} — {price_value} тенге")

        average_price = sum(prices) / len(prices)
        print(f"Средняя стоимость книг: {average_price:.2f} тенге")

except FileNotFoundError:
    print("Ошибка: файл 'books.txt' не найден.")
except Exception as err:
    print("Непредвиденная ошибка:", err)
    print("Работа программы завершена.")