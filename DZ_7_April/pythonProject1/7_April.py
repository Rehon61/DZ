# 1.
# get_top_students = lambda students: [student['name'] for student in students if (sum(student['math']) + sum(student['english'])) / 6 > 80]
# import random
#
# students = [
#     {'name': 'Alice', 'math': [random.randint(70, 90) for _ in range(3)], 'english': [random.randint(70, 90) for _ in range(3)]},
#     {'name': 'Bob', 'math': [random.randint(70, 90) for _ in range(3)], 'english': [random.randint(70, 90) for _ in range(3)]},
#     {'name': 'Eve', 'math': [random.randint(70, 90) for _ in range(3)], 'english': [random.randint(70, 90) for _ in range(3)]}
# ]
#
# top_students = get_top_students(students)
# print(top_students)

# 2.
# products = [
#     {'name': 'Apple', 'price': 1.5, 'quantity': 10},
#     {'name': 'Banana', 'price': 0.75, 'quantity': 20},
#     {'name': 'Cherry', 'price': 2, 'quantity': 5}
# ]
# get_total_cost = lambda products: sum(product['price'] * product['quantity'] for product in products)
# total_cost = get_total_cost(products)
# print(total_cost)

# 3.
# get_word_counts = lambda word_list: {word: word_list.count(word) for word in word_list}
# word_list = ["apple", "banana", "apple", "cherry", "banana", "apple"]
# word_counts = get_word_counts(word_list)
# print(word_counts)