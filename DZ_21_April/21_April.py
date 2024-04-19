
# 1. К уже реализованному классу «Дробь» добавьте статический метод,
# который при вызове возвращает количество созданных объектов класса «Дробь».

class Fraction:
    count = 0

    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        if denominator != 0:
            self.denominator = denominator
        else:
            raise ValueError("Знаменатель не может быть равен нулю")
        Fraction.count += 1  # Увеличиваем счетчик при создании нового объекта

    @staticmethod
    def get_instance_count():
        return Fraction.count



    def input_fraction(self):
        self.numerator = int(input("Введите числитель: "))
        self.denominator = int(input("Введите знаменатель: "))
        if self.denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю")

    def output_fraction(self):
        print(f"{self.numerator}/{self.denominator}")

    def add(self, other):
        result_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def subtract(self, other):
        result_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def multiply(self, other):
        result_numerator = self.numerator * other.numerator
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def divide(self, other):
        if other.numerator == 0:
            raise ValueError("Деление на ноль")
        result_numerator = self.numerator * other.denominator
        result_denominator = self.denominator * other.numerator
        return Fraction(result_numerator, result_denominator)


fraction1 = Fraction()
fraction2 = Fraction()

fraction1.input_fraction()
fraction2.input_fraction()

print("Первая дробь:")
fraction1.output_fraction()
print("Вторая дробь:")
fraction2.output_fraction()

sum_fraction = fraction1.add(fraction2)
print("Сумма дробей:")
sum_fraction.output_fraction()

difference_fraction = fraction1.subtract(fraction2)
print("Разность дробей:")
difference_fraction.output_fraction()

product_fraction = fraction1.multiply(fraction2)
print("Произведение дробей:")
product_fraction.output_fraction()

quotient_fraction = fraction1.divide(fraction2)
print("Частное дробей:")
quotient_fraction.output_fraction()

print("Количество созданных объектов класса Дробь:", Fraction.get_instance_count())





