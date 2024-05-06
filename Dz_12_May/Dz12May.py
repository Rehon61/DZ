# 1.
# def main():
#     number_list = []
#     while True:
#         print("\nМеню:")
#         print("1. Добавить новое число в список")
#         print("2. Удалить все вхождения числа из списка")
#         print("3. Показать содержимое списка (с начала или с конца)")
#         print("4. Проверить есть ли значение в списке")
#         print("5. Заменить значение в списке")
#         print("6. Выйти из программы")
#
#         choice = input("\nВведите номер выбранного пункта (1-6): ")
#
#         if choice == "1":
#             new_number = input("Введите новое число: ")
#             if new_number in number_list:
#                 print(f"\nЧисло {new_number} уже есть в списке.")
#             else:
#                 number_list.append(new_number)
#
#         elif choice == "2":
#             remove_number = input("Введите число для удаления: ")
#             while remove_number in number_list:
#                 number_list.remove(remove_number)
#
#         elif choice == "3":
#             show_from_start = input("Показать список с начала (да/нет)? ")
#             if show_from_start.lower() == "нет":
#                 number_list.reverse()
#
#             print("\nСодержимое списка:", number_list)
#
#             if show_from_start.lower() == "нет":
#                 number_list.reverse()
#
#         elif choice == "4":
#             check_number = input("Введите число для проверки: ")
#
#             if check_number in number_list:
#                 print(f"\nЧисло {check_number} есть в списке.")
#             else:
#                 print(f"\nЧисло {check_number} отсутствует в списке.")
#
#         elif choice == "5":
#             replace_number = input("Введите число для замены: ")
#
#             if replace_number in number_list:
#                 replace_with = input("Введите число для замены на: ")
#
#                 while replace_number in number_list:
#                     index = number_list.index(replace_number)
#                     number_list[index] = replace_with
#             else:
#                 print("\nЧисло для замены отсутствует в списке.")
#
#         elif choice == "6":
#             print("\nВыход из программы.")
#
#             break
#
#         else:
#             print("\nНеверный выбор. Пожалуйста, выберите номер от 1 до 6.")
#
#
# if __name__ == "__main__":
#     main()


# 2.
# class StringStack:
#     def __init__(self, max_size):
#         self.max_size = max_size
#         self.stack = []
#
#     def push(self, string):
#         if len(self.stack) < self.max_size:
#             self.stack.append(string)
#             print(f"Строка '{string}' добавлена в стек.")
#         else:
#             print("Стек полон. Невозможно добавить новую строку.")
#
#     def pop(self):
#         if not self.is_empty():
#             string = self.stack.pop()
#             print(f"Строка '{string}' выталкивана из стека.")
#         else:
#             print("Стек пуст. Невозможно выполнить выталкивание.")
#
#     def count(self):
#         return len(self.stack)
#
#     def is_empty(self):
#         return len(self.stack) == 0
#
#     def is_full(self):
#         return len(self.stack) == self.max_size
#
#     def clear(self):
#         self.stack = []
#         print("Стек очищен.")
#
#     def peek(self):
#         if not self.is_empty():
#             return self.stack[-1]
#         else:
#             print("Стек пуст. Возвращено значение None.")
#             return None
#
# def show_menu():
#     print("\nМеню:")
#     print("1. Поместить строку в стек")
#     print("2. Вытащить строку из стека")
#     print("3. Подсчитать количество строк в стеке")
#     print("4. Проверить, пустой ли стек")
#     print("5. Проверить, полный ли стек")
#     print("6. Очистить стек")
#     print("7. Получить значение верхней строки без выталкивания")
#     print("8. Выйти из программы")
#
# def main():
#     max_size = int(input("Введите максимальный размер стека: "))
#     stack = StringStack(max_size)
#
#     while True:
#         show_menu()
#         choice = input("\nВведите номер выбранного пункта (1-8): ")
#
#         if choice == "1":
#             string = input("Введите строку для помещения в стек: ")
#             stack.push(string)
#
#         elif choice == "2":
#             stack.pop()
#
#         elif choice == "3":
#             count = stack.count()
#             print(f"Количество строк в стеке: {count}")
#
#         elif choice == "4":
#             if stack.is_empty():
#                 print("Стек пуст.")
#             else:
#                 print("Стек не пуст.")
#
#         elif choice == "5":
#             if stack.is_full():
#                 print("Стек полон.")
#             else:
#                 print("Стек не полон.")
#
#         elif choice == "6":
#             stack.clear()
#
#         elif choice == "7":
#             top_string = stack.peek()
#             if top_string is not None:
#                 print(f"Значение верхней строки: {top_string}")
#
#         elif choice == "8":
#             print("Выход из программы.")
#             break
#
#         else:
#             print("Неверный выбор. Пожалуйста, выберите номер от 1 до 8.")
#
# if __name__ == "__main__":
#     main()

# 3.
# class StringStack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, string):
#         self.stack.append(string)
#         print(f"Строка '{string}' добавлена в стек.")
#
#     def pop(self):
#         if not self.is_empty():
#             string = self.stack.pop()
#             print(f"Строка '{string}' выталкивана из стека.")
#         else:
#             print("Стек пуст. Невозможно выполнить выталкивание.")
#
#     def count(self):
#         return len(self.stack)
#
#     def is_empty(self):
#         return len(self.stack) == 0
#
#     def clear(self):
#         self.stack = []
#         print("Стек очищен.")
#
#     def peek(self):
#         if not self.is_empty():
#             return self.stack[-1]
#         else:
#             print("Стек пуст. Возвращено значение None.")
#             return None
#
#
# stack = StringStack()
# stack.push("Привет")
# stack.push("Мир")
# stack.pop()
# stack.clear()



