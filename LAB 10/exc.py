try:
    with open(r"C:\Users\Аяжан\OneDrive\Desktop\Әлібек Сабак\LAB 10\книги.txt", "r", encoding="utf-8") as file:
        data = file.readlines()
        print("Файл найден. Чтение выполнено.")
except FileNotFoundError:
    print("Ошибка: указанный файл не существует.")
except Exception as err:
    print("Произошла непредвиденная ошибка:", err)
else:
    print("Чтение файла завершено без ошибок.")
finally:
    print("Работа программы окончена.")

