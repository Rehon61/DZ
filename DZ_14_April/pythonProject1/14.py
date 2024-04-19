# 1.
# def compare_files(file1_path, file2_path):
#     with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
#         lines1 = file1.readlines()
#         lines2 = file2.readlines()
#
#     min_len = min(len(lines1), len(lines2))
#
#     for i in range(min_len):
#         if lines1[i] != lines2[i]:
#             print(f"Файл 1: {lines1[i]}")
#             print(f"Файл 2: {lines2[i]}")
#
#     if len(lines1) > len(lines2):
#         for i in range(min_len, len(lines1)):
#             print(f"Файл 1: {lines1[i]}")
#     elif len(lines2) > len(lines1):
#         for i in range(min_len, len(lines2)):
#             print(f"Файл 2: {lines2[i]}")
#
#
# file1_path = 'file1.txt'
# file2_path = 'file2.txt'
#
# compare_files(file1_path, file2_path)

# 2.
# def get_statistics(input_file_path, output_file_path):
#
#     with open(input_file_path, 'r') as file:
#
#         content = file.read()
#
#         num_chars = len(content)
#         num_lines = content.count('\n') + 1
#         vowels = 'aeiouAEIOU'
#         consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
#         digits = '0123456789'
#
#         num_vowels = sum(1 for char in content if char in vowels)
#         num_consonants = sum(1 for char in content if char in consonants)
#         num_digits = sum(1 for char in content if char in digits)
#
#
#         with open(output_file_path, 'w') as output_file:
#             output_file.write(f"Количество символов: {num_chars}\n")
#             output_file.write(f"Количество строк: {num_lines}\n")
#             output_file.write(f"Количество гласных букв: {num_vowels}\n")
#             output_file.write(f"Количество согласных букв: {num_consonants}\n")
#             output_file.write(f"Количество цифр: {num_digits}\n")
#
# input_file_path = 'input.txt'
# output_file_path = 'statistics.txt'
# get_statistics(input_file_path, output_file_path)


# 3.
# with open('test1.txt', 'r') as f:
#     lines = f.readlines()
#
# with open('test2.txt', 'w') as f:
#     for line in lines[:-1]:
#         f.write(line)

# 4.
# with open("text_file.txt", "r") as file:
#     max_length = 0
#     for line in file:
#         length = len(line)
#         if length > max_length:
#             max_length = length
#
# print("Длина самой длинной строки:", max_length)

# 5.

# with open('text.txt', 'r') as f:
#     text = f.read()
# word = input("Введите слово для поиска: ")
# count = text.count(word)
# print(f"Слово '{word}' встречается в тексте {count} раз.")


# 6.
# with open('search.txt', 'r+') as f:
#     contents = f.read()
#     find_word = input("Введите слово для поиска: ")
#     replace_word = input("Введите слово для замены: ")
#     contents = contents.replace(find_word, replace_word)
#     f.seek(0)
#     f.write(contents)



