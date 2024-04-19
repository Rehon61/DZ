# 1.
# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (3, 4, 5, 6, 7)
# tuple3 = (4, 5, 6, 7, 8)
#
# set1 = set(tuple1)
# set2 = set(tuple2)
# set3 = set(tuple3)
# common_elements = set1 & set2 & set3
# common_elements_tuple = tuple(common_elements)
#
# print(common_elements_tuple)




# 2.

# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (3, 4, 5, 6, 7)
# tuple3 = (4, 5, 6, 7, 8)
#
# set1 = set(tuple1)
# set2 = set(tuple2)
# set3 = set(tuple3)
#
# unique_elements = set1 ^ set2 ^ set3
#
# unique_elements_tuple = tuple(unique_elements)
#
# print(unique_elements_tuple)


# 3.

# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (1, 2, 3, 4, 5)
# tuple3 = (1, 2, 3, 4, 5)

# tuple1 = (11, 2, 3, 4, 5)
# tuple2 = (1, 2, 3, 4, 5)
# tuple3 = (14, 2, 3, 4, 5)
#
# zipped_tuples = zip(tuple1, tuple2, tuple3)
#
# common_elements_at_same_position = all(all(element == zipped_tuple[0] for element in zipped_tuple) for zipped_tuple in zipped_tuples)
#
# if common_elements_at_same_position:
#     print("Да, существуют элементы, которые есть в каждом из кортежей и находятся на той же позиции.")
# else:
#     print("Нет, нет элементов, которые есть в каждом из кортежей и находятся на той же позиции.")


