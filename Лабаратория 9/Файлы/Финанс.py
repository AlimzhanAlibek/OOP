import os

file_path = r"C:\Users\Student\Project\Лабаратория 9\Файлы\Доходы.txt"
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# Создание файла с начальными доходами, если его нет
if not os.path.exists(file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Operator - 150000 тг\n")
        file.write("Manager - 200000 тг\n")

print("Файл создан и записан!")

# Чтение всех доходов из файла
incomes = {}
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if " - " in line:
            try:
                job, amount_str = line.split(" - ")
                amount = int(amount_str.replace("тг", "").strip())
                incomes[job] = amount
            except ValueError:
                print(f"Ошибка преобразования числа для строки: {line}")

# Отображение всех доступных позиций и выбор оператора
print("\nДоступные работы:")
for i, job in enumerate(incomes.keys(), 1):
    print(f"{i}. {job}")

while True:
    try:
        selected_index = int(input("\nВыберите номер работы для обновления или введите 0 для добавления новой работы: ")) - 1
        if selected_index == -1:
            # Ввод новой работы
            new_job_name = input("\nВведите название новой работы: ").strip()
            while True:
                new_salary_input = input(f"Введите зарплату для {new_job_name}: ").strip()
                try:
                    new_salary = int(new_salary_input)
                    if new_salary < 50000:
                        raise ValueError("Сумма слишком маленькая!")
                    break
                except ValueError as e:
                    print("Ошибка:", e)

            incomes[new_job_name] = new_salary
            print(f"Новая работа {new_job_name} с доходом {new_salary} тг добавлена!")
            break
        elif 0 <= selected_index < len(incomes):
            selected_job = list(incomes.keys())[selected_index]
            break
        else:
            print("Ошибка: Неверный номер, попробуйте снова.")
    except ValueError:
        print("Ошибка: Введите корректный номер.")

# Ввод нового дохода для выбранной работы
if selected_index != -1:
    while True:
        new_salary_input = input(f"Введите новую сумму зарплаты для {selected_job}: ").strip()
        try:
            new_salary = int(new_salary_input)
            if new_salary < 50000:
                raise ValueError("Сумма слишком маленькая!")
            break
        except ValueError as e:
            print("Ошибка:", e)

    # Обновление дохода для выбранной работы
    incomes[selected_job] = new_salary
    print(f"Зарплата для {selected_job} обновлена на {new_salary} тг.")

# Перезапись файла с обновленными доходами
with open(file_path, "w", encoding="utf-8") as file:
    for job, amount in incomes.items():
        file.write(f"{job} - {amount} тг\n")

print("\nОбновленный список доходов:")
for job, amount in incomes.items():
    print(f"{job} — {amount} тг")

total_income = sum(incomes.values())
print(f"\nОбщий доход: {total_income} тг")
