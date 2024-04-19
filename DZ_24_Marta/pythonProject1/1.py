# 1.
# def product_of_elements(lst):
#     product = 1
#     for num in lst:
#         product *= num
#     return product
#
#
# numbers = [1, 2, 3, 4, 5]
# print(product_of_elements(numbers))

# 2.
# def find_minimum(lst):
#     if lst:
#         return min(lst)
#     else:
#         return None  #
# numbers = [5, 3, 9, 1, 2]
# print(find_minimum(numbers))

# 3.
# def is_prime(n):
#     if n <= 1:
#         return False
#     elif n <= 3:
#         return True
#     elif n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True
#
# def count_primes(lst):
#     count = 0
#     for num in lst:
#         if is_prime(num):
#             count += 1
#     return count
# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(count_primes(numbers))  # должно вывести 4

# 4.
# def remove_element(lst, num):
#     count = 0
#     while num in lst:
#         lst.remove(num)
#         count += 1
#     return count
# numbers = [1, 2, 3, 2, 4, 2, 5]
# print(remove_element(numbers, 2))

# 5.
# def combine_lists(lst1, lst2):
#     return lst1 + lst2
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# print(combine_lists(list1, list2))


# 6.
# def power_elements(lst, power):
#     return [num ** power for num in lst]
# numbers = [1, 2, 3, 4, 5]
# print(power_elements(numbers, 2))
