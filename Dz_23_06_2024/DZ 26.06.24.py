# import json
#
# class Ingredient:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class HotDog:
#     def __init__(self, base_price=3.0):
#         self.base_price = base_price
#         self.ingredients = []
#
#     def add_ingredient(self, ingredient):
#         self.ingredients.append(ingredient)
#
#     def calculate_price(self):
#         return self.base_price + sum(ingredient.price for ingredient in self.ingredients)
#
#     def __str__(self):
#         ingredients_str = ", ".join(ingredient.name for ingredient in self.ingredients) if self.ingredients else "Без добавок"
#         return f"Хот-дог: {ingredients_str}, Цена: 💲{self.calculate_price():.2f}"
#
# def print_colored(text, color):
#     colors = {
#         "black": "\u001b[30m",
#         "red": "\u001b[31m",
#         "green": "\u001b[32m",
#         "yellow": "\u001b[33m",
#         "blue": "\u001b[34m",
#         "magenta": "\u001b[35m",
#         "cyan": "\u001b[36m",
#         "white": "\u001b[37m",
#         "reset": "\u001b[0m"
#     }
#     color_code = colors.get(color.lower(), colors["reset"])
#     return f"{color_code}{text}{colors['reset']}"
#
# class Order:
#     def __init__(self, payment_method):
#         self.hotdogs = []
#         self.payment_method = payment_method
#
#     def add_hotdog(self, hotdog):
#         self.hotdogs.append(hotdog)
#
#     def calculate_total(self):
#         total = sum(hotdog.calculate_price() for hotdog in self.hotdogs)
#         discount = 0.1 if len(self.hotdogs) >= 3 else 0
#         if discount > 0:
#             discount_message = print_colored("🎉Вы получили скидку 10% на заказ от трех хот-догов!🎉", "green")
#             print(discount_message)
#         return total * (1 - discount)
#
#     def __str__(self):
#         hotdogs_str = "\n".join(str(hotdog) for hotdog in self.hotdogs)
#         return f"Заказ:\n{hotdogs_str}\nИтого: 💲{self.calculate_total():.2f}, Метод оплаты: {self.payment_method}\n❤️Приятного аппетита!❤️\n\n"
#
# class Kiosk:
#     def __init__(self):
#         self.orders = []
#         self.ingredients = {
#             'Майонез': Ingredient('Майонез', 0.2),
#             'Горчица': Ingredient('Горчица', 0.1),
#             'Кетчуп': Ingredient('Кетчуп', 0.1),
#
#         }
#         self.stock = {
#             'Майонез': 20,
#             'Горчица': 20,
#             'Кетчуп': 20,
#
#         }
#
#     def check_ingredients(self):
#         print("Список ингредиентов в наличии:")
#         for name, ingredient in self.ingredients.items():
#             quantity = self.check_stock(name)
#             price = ingredient.price
#             print(f"{name}: {quantity} шт, Цена за единицу: 💲{price:.2f}")
#
#     def create_order(self, payment_method):
#         return Order(payment_method)
#
#     def save_order(self, order):
#         self.orders.append(order)
#         with open('orders.json', 'a') as f:
#             json.dump(order, f, default=lambda o: o.__dict__, indent=4)
#             f.write('\n')
#
#     def get_statistics(self):
#         total_hotdogs = sum(len(order.hotdogs) for order in self.orders)
#         total_revenue = sum(order.calculate_total() for order in self.orders)
#         total_profit = total_revenue * 0.2
#         return {
#             "total_hotdogs": total_hotdogs,
#             "total_revenue": total_revenue,
#             "total_profit": total_profit,
#         }
#
#     def check_stock(self, ingredient_name):
#         return self.stock.get(ingredient_name, 0)
#
#
# def main():
#     kiosk = Kiosk()
#     while True:
#         print("Добро пожаловать в киоск хот-догов!")
#         print("1. Создать заказ")
#         print("2. Просмотреть статистику")
#         print("3. Проверить наличие ингредиентов")
#         print("4. Выход")
#         user_choice = input("Введите номер действия: ")
#         if user_choice == '1':
#             payment_method = input("Введите метод оплаты: ")
#             order = kiosk.create_order(payment_method)
#             while True:
#                 hotdog = HotDog()
#                 print("Добавьте ингредиенты в хот-дог:")
#                 for name in kiosk.ingredients:
#                     print(f"Добавить {name}? (да/нет)")
#                     choice = input()
#                     if choice.lower() == 'да':
#                         hotdog.add_ingredient(kiosk.ingredients[name])
#                 order.add_hotdog(hotdog)
#                 another = input("Добавить еще один хот-дог? (да/нет)")
#                 if another.lower() != 'да':
#                     break
#             kiosk.save_order(order)
#             print("Заказ создан!\n")
#             print(order)
#         elif user_choice == '2':
#             stats = kiosk.get_statistics()
#             print(f"Всего продано хот-догов: {stats['total_hotdogs']}")
#             print(f"Выручка: 💲{stats['total_revenue']:.2f}")
#             print(f"Прибыль: 💲{stats['total_profit']:.2f}")
#         elif user_choice == '3':
#             kiosk.check_ingredients()
#         elif user_choice == '4':
#             print("Спасибо за визит в наш киоск ^_^. До свидания! <3")
#             break
#         else:
#             print("Неверный выбор. Попробуйте снова.")
#
# if __name__ == "__main__":
#     main()
