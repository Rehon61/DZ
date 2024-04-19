# 1.
# players = {}
#
# def new_player():
#     name = input("Введите ФИО баскетболиста: ")
#     rost = float(input("Введите рост баскетболиста (в метрах): "))
#     players[name] = rost
#
# def del_player():
#     name = input("Введите ФИО баскетболиста, которого хотите удалить: ")
#     if name in players:
#         del players[name]
#         print("Игрок удален.")
#     else:
#         print("Такого игрока нет в списке.")
#
#
# def found_player():
#     name = input("Введите ФИО баскетболиста, которого хотите найти: ")
#     if name in players:
#         print("Данные об игроке:")
#         print("ФИО:", name)
#         print("Рост:", players[name])
#     else:
#         print("Такого игрока нет в списке.")
#
# def replacement():
#     name = input("Введите ФИО баскетболиста, данные которого хотите заменить: ")
#     if name in players:
#         rost = float(input("Введите новый рост баскетболиста (в метрах): "))
#         players[name] = rost
#         print("Данные заменены.")
#     else:
#         print("Такого игрока нет в списке.")
#
#
# while True:
#     print("Выберите действие:")
#     print("1. Добавить игрока")
#     print("2. Удалить игрока")
#     print("3. Найти игрока")
#     print("4. Заменить данные")
#     print("5. Выход")
#
#     сhoice = int(input("Введите номер действия: "))
#
#     if сhoice == 1:
#         new_player()
#     elif сhoice == 2:
#         del_player()
#     elif сhoice == 3:
#         found_player()
#     elif сhoice == 4:
#         replacement()
#     elif сhoice == 5:
#         break
#     else:
#         print("Неверный ввод.")

# 3.
# employees = {}
#
# def add_employee():
#     name = input("Введите полное имя сотрудника: ")
#     phone = input("Введите номер телефона сотрудника: ")
#     email = input("Введите рабочий адрес электронной почты сотрудника ")
#     position = input("Введите должность сотрудника: ")
#     office_number = input("Введите номер кабинета сотрудника: ")
#     skype = input("Введите имя пользователя Skype сотрудника: ")
#     employees[name] = {
#         "телефон": phone,
#         "email": email,
#         "должность": position,
#         "номер офиса": office_number,
#         "skype": skype,
#     }
#
#
# def delete_employee():
#     name = input("Введите полное имя сотрудника, которого хотите удалить: ")
#     if name in employees:
#         del employees[name]
#         print("Сотрудник удален.")
#     else:
#         print("В списке нет такого сотрудника.")
#
#
# def find_employee():
#     name = input("Введите полное имя сотрудника, которого хотите найти: ")
#     if name in employees:
#         print("Данные о сотруднике:")
#         print("Полное имя", name)
#         for key, value in employees[name].items():
#             print(f"{key}: {value}")
#     else:
#         print("В списке нет такого сотрудника.")
#
#
# def update_data():
#     name = input("Введите ФИО сотрудника, данные которого вы хотите обновить: ")
#     if name in employees:
#         key = input("Введите ключ, который вы хотите изменить: ")
#         if key in employees[name]:
#             value = input("Введите новое значение: ")
#             employees[name][key] = value
#             print("Данные обновлены.")
#         else:
#             print("В данных сотрудника такого ключа нет.")
#     else:
#         print("В списке нет такого сотрудника.")
#
#
# while True:
#     print("Выберите действие:")
#     print("1. Добавить сотрудника")
#     print("2. Удалить сотрудника")
#     print("3. Найти сотрудника")
#     print("4. Обновить данные")
#     print("5. Выйти")
#
#     choice = int(input("Введите номер действия: "))
#
#     if choice == 1:
#         add_employee()
#     elif choice == 2:
#         delete_employee()
#     elif choice == 3:
#         find_employee()
#     elif choice == 4:
#         update_data()
#     elif choice == 5:
#         break
#     else:
#         print("Неверный Ввод.")