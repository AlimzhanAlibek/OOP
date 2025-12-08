file_path = r"C:\Users\Аяжан\OneDrive\Desktop\Әлібек Сабак\LAB 10\книги.txt"

title = input("Введите название книги: ")
price = input("Введите цену книги: ")

if not price.isdigit():
    print("Ошибка: цена должна быть числом.")
else:
    try:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(f"\n{title}, {price}")
        print("Запись успешно добавлена!")

        print("\nОбновлённый список книг:")
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                print(line.strip())

    except Exception as e:
        print("Произошла ошибка при работе с файлом:", e)
