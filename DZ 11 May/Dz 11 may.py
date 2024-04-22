# 1.
# import time
#
# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print("Time taken: {:.6f}s".format(end_time - start_time))
#         return result
#     return wrapper
#
# @measure_time
# def get_primes():
#     primes = []
#     for num in range(2, 1001):
#         is_prime = True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
#     return primes
#
# primes_list = get_primes()
# print("Primes:", primes_list)

# 2.
# import time
#
# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print("Time taken: {:.6f}s".format(end_time - start_time))
#         return result
#     return wrapper
#
# @measure_time
# def get_primes(lower_limit, upper_limit):
#     primes = []
#     for num in range(lower_limit, upper_limit + 1):
#         if num > 1:
#             is_prime = True
#             for i in range(2, int(num ** 0.5) + 1):
#                 if num % i == 0:
#                     is_prime = False
#                     break
#             if is_prime:
#                 primes.append(num)
#     return primes
#
# lower_limit = int(input("Enter lower limit: "))
# upper_limit = int(input("Enter upper limit: "))
#
# primes_list = get_primes(lower_limit, upper_limit)
# print("Primes:", primes_list)

# 3.
# def handle_exceptions(func):
#     def wrapper(*args, **kwargs):
#         try:
#             result = func(*args, **kwargs)
#         except Exception as e:
#             print("Error:", e)
#             result = None
#         return result
#     return wrapper
#
#
# @handle_exceptions
# def divide(a, b):
#     return a / b
#
# result = divide(10, 0)
# print("Result:", result)

# 4.
# def add_method(cls):
#     def new_method(self, value):
#         return value ** 2
#     cls.new_method = new_method
#     return cls
#
# @add_method
# class MyClass:
#     pass
#
# obj = MyClass()
# result = obj.new_method(5)
# print("Result:", result)





