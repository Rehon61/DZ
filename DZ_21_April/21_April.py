
# 1. К уже реализованному классу «Дробь» добавьте статический метод,
# который при вызове возвращает количество созданных объектов класса «Дробь».

# class Fraction:
#     count = 0
#
#     def __init__(self, numerator=0, denominator=1):
#         self.numerator = numerator
#         if denominator != 0:
#             self.denominator = denominator
#         else:
#             raise ValueError("Знаменатель не может быть равен нулю")
#         Fraction.count += 1  # Увеличиваем счетчик при создании нового объекта
#
#     @staticmethod
#     def get_instance_count():
#         return Fraction.count
#
#
#
#     def input_fraction(self):
#         self.numerator = int(input("Введите числитель: "))
#         self.denominator = int(input("Введите знаменатель: "))
#         if self.denominator == 0:
#             raise ValueError("Знаменатель не может быть равен нулю")
#
#     def output_fraction(self):
#         print(f"{self.numerator}/{self.denominator}")
#
#     def add(self, other):
#         result_numerator = self.numerator * other.denominator + other.numerator * self.denominator
#         result_denominator = self.denominator * other.denominator
#         return Fraction(result_numerator, result_denominator)
#
#     def subtract(self, other):
#         result_numerator = self.numerator * other.denominator - other.numerator * self.denominator
#         result_denominator = self.denominator * other.denominator
#         return Fraction(result_numerator, result_denominator)
#
#     def multiply(self, other):
#         result_numerator = self.numerator * other.numerator
#         result_denominator = self.denominator * other.denominator
#         return Fraction(result_numerator, result_denominator)
#
#     def divide(self, other):
#         if other.numerator == 0:
#             raise ValueError("Деление на ноль")
#         result_numerator = self.numerator * other.denominator
#         result_denominator = self.denominator * other.numerator
#         return Fraction(result_numerator, result_denominator)
#
#
# fraction1 = Fraction()
# fraction2 = Fraction()
#
# fraction1.input_fraction()
# fraction2.input_fraction()
#
# print("Первая дробь:")
# fraction1.output_fraction()
# print("Вторая дробь:")
# fraction2.output_fraction()
#
# sum_fraction = fraction1.add(fraction2)
# print("Сумма дробей:")
# sum_fraction.output_fraction()
#
# difference_fraction = fraction1.subtract(fraction2)
# print("Разность дробей:")
# difference_fraction.output_fraction()
#
# product_fraction = fraction1.multiply(fraction2)
# print("Произведение дробей:")
# product_fraction.output_fraction()
#
# quotient_fraction = fraction1.divide(fraction2)
# print("Частное дробей:")
# quotient_fraction.output_fraction()
#
# print("Количество созданных объектов класса Дробь:", Fraction.get_instance_count())


# 2. Создайте класс для конвертирования температуры из
# Цельсия в Фаренгейт и наоборот. У класса должно быть
# два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий. Также
# класс должен считать количество подсчетов температурыи
# возвращать это значение с помощью статического метода.

# class TemperatureConverter:
#     conversion_count = 0
#
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         TemperatureConverter.conversion_count += 1
#         return (celsius * 9/5) + 32
#
#     @staticmethod
#     def fahrenheit_to_celsius(fahrenheit):
#         TemperatureConverter.conversion_count += 1
#         return (fahrenheit - 32) * 5/9
#
#     @staticmethod
#     def get_conversion_count():
#         return TemperatureConverter.conversion_count
#
#
#
# celsius_temp = 30
# fahrenheit_result = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
# print(f"{celsius_temp} градусов Цельсия = {fahrenheit_result} градусов Фаренгейта")
#
#
# fahrenheit_temp = 86
# celsius_result = TemperatureConverter.fahrenheit_to_celsius(fahrenheit_temp)
# print(f"{fahrenheit_temp} градусов Фаренгейта = {celsius_result} градусов Цельсия")
#
#
# print("Количество конвертаций:", TemperatureConverter.get_conversion_count())

# 3.Создайте класс для перевода из метрической системы
# в английскую и наоборот. Функциональность необходимо
# реализовать в виде статических методов. Обязательно
# реализуйте перевод мер длины.

# class LengthConverter:
#     @staticmethod
#     def meters_to_feet(meters):
#         return meters * 3.28084
#
#     @staticmethod
#     def feet_to_meters(feet):
#         return feet / 3.28084
#
#     @staticmethod
#     def meters_to_miles(meters):
#         return meters / 1609.344
#
#     @staticmethod
#     def miles_to_meters(miles):
#         return miles * 1609.344
#
#
#
# meters_value = 100
# feet_result = LengthConverter.meters_to_feet(meters_value)
# print(f"{meters_value} метров = {feet_result:.2f} футов")
#
#
# feet_value = 328.084
# meters_result = LengthConverter.feet_to_meters(feet_value)
# print(f"{feet_value} футов = {meters_result:.2f} метров")
#
#
# meters_value = 1609.344
# miles_result = LengthConverter.meters_to_miles(meters_value)
# print(f"{meters_value} метров = {miles_result:.2f} миль")
#
#
# miles_value = 1
# meters_result = LengthConverter.miles_to_meters(miles_value)
# print(f"{miles_value} миль = {meters_result:.2f} метров")






