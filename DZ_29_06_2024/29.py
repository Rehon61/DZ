# 1.
# import threading
# import random
# import time
#
# numbers_list = []
#
# condition = threading.Condition()
#
#
# def fill_list():
#     with condition:
#         print("Запуск потока для заполнения списка...", flush=True)
#         for _ in range(10):
#             num = random.randint(1, 100)
#             numbers_list.append(num)
#             time.sleep(0.1)
#         print(f"Список заполнен: {numbers_list}", flush=True)
#         condition.notify_all()
#
#
# def calculate_sum():
#     with condition:
#         print("Поток для расчета суммы ожидает...", flush=True)
#         condition.wait_for(lambda: len(numbers_list) == 10)
#         sum_of_numbers = sum(numbers_list)
#         print(f"Сумма элементов списка: {sum_of_numbers}", flush=True)
#
# def calculate_average():
#     with condition:
#         print("Поток для расчета среднего ожидает...", flush=True)
#         condition.wait_for(lambda: len(numbers_list) == 10)
#         average = sum(numbers_list) / len(numbers_list)
#         print(f"Среднеарифметическое значение элементов списка: {average}", flush=True)
#
#
# fill_thread = threading.Thread(target=fill_list)
# sum_thread = threading.Thread(target=calculate_sum)
# average_thread = threading.Thread(target=calculate_average)
#
# fill_thread.start()
# sum_thread.start()
# average_thread.start()
#
#
# fill_thread.join()
# sum_thread.join()
# average_thread.join()





# 2.

# import threading
# import random
# import math
#
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# def generate_numbers(file_path, count=100):
#     with open(file_path, 'w') as f:
#         for _ in range(count):
#             f.write(f"{random.randint(1, 100)}\n")
#     print("Файл заполнен случайными числами.")
#
# def find_primes(file_path, result_path):
#     with open(file_path, 'r') as f:
#         numbers = [int(x) for x in f.readlines()]
#     primes = [x for x in numbers if is_prime(x)]
#     with open(result_path, 'w') as f:
#         for prime in primes:
#             f.write(f"{prime}\n")
#     print("Простые числа найдены.")
#
# def calculate_factorials(file_path, result_path):
#     with open(file_path, 'r') as f:
#         numbers = [int(x) for x in f.readlines()]
#     factorials = {x: math.factorial(x) for x in numbers}
#     with open(result_path, 'w') as f:
#         for number, factorial in factorials.items():
#             f.write(f"{number}: {factorial}\n")
#     print("Факториалы чисел вычислены.")
#
# def main():
#     file_path = input("Введите путь к файлу: ").strip('"')
#     primes_path = "primes.txt"
#     factorials_path = "factorials.txt"
#
#     generator_thread = threading.Thread(target=generate_numbers, args=(file_path,))
#     primes_thread = threading.Thread(target=find_primes, args=(file_path, primes_path))
#     factorials_thread = threading.Thread(target=calculate_factorials, args=(file_path, factorials_path))
#
#     generator_thread.start()
#     generator_thread.join()
#
#     primes_thread.start()
#     factorials_thread.start()
#
#     primes_thread.join()
#     factorials_thread.join()
#
#     print("Операции завершены.")
#
# if __name__ == "__main__":
#     main()



# 3.

# import shutil
# import os
# import threading
#
#
# def copy_directory(src, dst):
#     try:
#
#         shutil.copytree(src, dst)
#         print(f'Содержимое директории {src} успешно скопировано в {dst}')
#
#
#         num_files = sum(len(files) for _, _, files in os.walk(dst))
#         print(f'Всего файлов скопировано: {num_files}')
#     except Exception as e:
#         print(f'Произошла ошибка: {e}')
#
#
#
# source_path = input('Введите путь к существующей директории: ')
# destination_path = input('Введите путь к новой директории: ')
#
#
# copy_thread = threading.Thread(target=copy_directory, args=(source_path, destination_path))
# copy_thread.start()



# 4.

# import os
# import re
#
#
# def search_and_merge(src_directory, search_word, output_file):
#     merged_content = ''
#     for root, dirs, files in os.walk(src_directory):
#         for file in files:
#             file_path = os.path.join(root, file)
#             with open(file_path, 'r', encoding='utf-8') as f:
#                 file_content = f.read()
#                 if search_word in file_content:
#                     merged_content += file_content + '\n'
#     with open(output_file, 'w', encoding='utf-8') as f:
#         f.write(merged_content)
#
#
# def remove_forbidden_words(output_file, forbidden_words_file):
#     with open(forbidden_words_file, 'r', encoding='utf-8') as f:
#         forbidden_words = f.read().splitlines()
#     with open(output_file, 'r', encoding='utf-8') as f:
#         content = f.read()
#     for word in forbidden_words:
#
#         content = re.sub(r'\b' + re.escape(word) + r'\b', '', content)
#     with open(output_file, 'w', encoding='utf-8') as f:
#         f.write(content)
#
#
# src_directory = input('Введите путь к существующей директории: ')
# search_word = input('Введите слово для поиска: ')
# output_file = 'merged_content.txt'
# forbidden_words_file = 'forbidden_words.txt'
#
#
# search_and_merge(src_directory, search_word, output_file)
# remove_forbidden_words(output_file, forbidden_words_file)
#
#
# print(f'Файлы, содержащие слово "{search_word}", были найдены и объединены в файл "{output_file}".')
# print(f'Запрещенные слова были удалены из файла "{output_file}".')






