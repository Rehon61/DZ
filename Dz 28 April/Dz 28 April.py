# 1.
# import math
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def __eq__(self, other):
#         return self.radius == other.radius
#
#     def __lt__(self, other):
#         return self.radius < other.radius
#
#     def __le__(self, other):
#         return self.radius <= other.radius
#
#     def __gt__(self, other):
#         return self.radius > other.radius
#
#     def __ge__(self, other):
#         return self.radius >= other.radius
#
#     def __add__(self, value):
#         return Circle(self.radius + value)
#
#     def __iadd__(self, value):
#         self.radius += value
#         return self
#
#     def __sub__(self, value):
#         if (self.radius - value) < 0:
#             raise ValueError("Radius cannot be negative")
#         else:
#             return Circle(self.radius - value)
#
#     def __isub__(self, value):
#         if (self.radius - value) < 0:
#             raise ValueError("Radius cannot be negative")
#         else:
#             self.radius -= value
#             return self
#
#
# # Создаем две окружности
# circle1 = Circle(5)
# circle2 = Circle(10)
#
# # Проверяем равенство радиусов двух окружностей
# print(circle1 == circle2)  # False
#
# # Сравниваем длины двух окружностей
# print(circle1 < circle2)  # True
# print(circle1 > circle2)  # False
#
# # Изменяем размер первой окружности путем добавления значения к ее радиусу
# circle1 += 3
# print(circle1.radius)  # 8
#
# # Изменяем размер второй окружности путем вычитания значения из ее радиуса
# circle2 -= 5
# print(circle2.radius)  # 5
#
# try:
#     circle1 -= 10
# except ValueError as e:
#     print(e)


# 2.
# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
#
#     def __add__(self, other):
#         return Complex(self.real + other.real, self.imag + other.imag)
#
#     def __sub__(self, other):
#         return Complex(self.real - other.real, self.imag - other.imag)
#
#     def __mul__(self, other):
#         return Complex(self.real * other.real - self.imag * other.imag,
#                        self.real * other.imag + self.imag * other.real)
#
#     def __truediv__(self, other):
#         denominator = float(other.real ** 2 + other.imag ** 2)
#         return Complex((self.real * other.real + self.imag * other.imag) / denominator,
#                        (self.imag * other.real - self.real * other.imag) / denominator)
#
#     def __str__(self):
#         if self.imag >= 0:
#             return f"{self.real}+{self.imag}i"
#         else:
#             return f"{self.real}{self.imag}i"
#
#
# c1 = Complex(1, 2)
# c2 = Complex(3, 4)
# print(c1 + c2) # (1+2i) + (3+4i) = 4+6i
# print(c1 - c2) # (1+2i) - (3+4i) = -2-2i
# print(c1 * c2) # (1+2i) * (3+4i) = -5+10i
# print(c1 / c2) # (1+2i) / (3+4i) = 0.44+0.08i

# 3.
# class Airplane:
#     def __init__(self, model, max_passengers, current_passengers=0):
#         self.model = model
#         self.max_passengers = max_passengers
#         self.current_passengers = current_passengers
#
#     def __eq__(self, other):
#         return isinstance(other, Airplane) and self.model == other.model
#
#     def __add__(self, value):
#         if (self.current_passengers + value) > self.max_passengers:
#             raise ValueError("Too many passengers")
#         else:
#             return Airplane(self.model, self.max_passengers, self.current_passengers + value)
#
#     def __iadd__(self, value):
#         if (self.current_passengers + value) > self.max_passengers:
#             raise ValueError("Too many passengers")
#         else:
#             self.current_passengers += value
#             return self
#
#     def __sub__(self, value):
#         if (self.current_passengers - value) < 0:
#             raise ValueError("Cannot have negative passengers")
#         else:
#             return Airplane(self.model, self.max_passengers, self.current_passengers - value)
#
#     def __isub__(self, value):
#         if (self.current_passengers - value) < 0:
#             raise ValueError("Cannot have negative passengers")
#         else:
#             self.current_passengers -= value
#             return self
#
#     def __lt__(self, other):
#         return isinstance(other, Airplane) and self.max_passengers < other.max_passengers
#
#     def __le__(self, other):
#         return isinstance(other, Airplane) and self.max_passengers <= other.max_passengers
#
#     def __gt__(self, other):
#         return isinstance(other, Airplane) and self.max_passengers > other.max_passengers
#
#     def __ge__(self, other):
#         return isinstance(other, Airplane) and self.max_passengers >= other.max_passengers
#
#
# # Создаем два самолета с разными моделями и максимальным количеством пассажиров на борту.
# airplane1 = Airplane("Boeing 747", 416)
# airplane2 = Airplane("Airbus A380", 853)
#
# # Проверяем равенство типов самолетов.
# print(airplane1 == airplane2)  # False
#
# # Увеличиваем количество пассажиров на борту первого самолета.
# airplane1 += 100
#
# # Сравниваем два самолета по максимально возможному количеству пассажиров на борту.
# print(airplane1 < airplane2)  # True
#
# # Уменьшаем количество пассажиров на борту первого самолета.
# airplane1 -= 50
#
# # Сравниваем два самолета по максимально возможному количеству пассажиров на борту.
# print(airplane1 >= airplane2)  # False

# 4.
# class Flat:
#     def __init__(self, area, price):
#         self.area = area
#         self.price = price
#
#     def __eq__(self, other):
#         return isinstance(other, Flat) and self.area == other.area
# 
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __lt__(self, other):
#         return isinstance(other, Flat) and self.price < other.price
#
#     def __le__(self, other):
#         return isinstance(other, Flat) and self.price <= other.price
#
#     def __gt__(self, other):
#         return isinstance(other, Flat) and self.price > other.price
#
#     def __ge__(self, other):
#         return isinstance(other, Flat) and self.price >= other.price
#
#
# flat1 = Flat(80, 100000)
# flat2 = Flat(75, 95000)
#
# # Проверка равенства площадей квартир
# print(flat1 == flat2)  # False
#
# # Проверка неравенства площадей квартир
# print(flat1 != flat2)  # True
#
# # Сравнение квартир по цене
# print(flat1 > flat2)  # True
# print(flat1 < flat2)  # False
# print(flat1 >= flat2)  # True
# print(flat1 <= flat2)  # False


