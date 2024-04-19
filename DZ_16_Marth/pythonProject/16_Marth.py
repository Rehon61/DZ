# print('''
# МЕНЮ ФИГУР!!!
# *****      *         *********           *              *****
#  ****      **         *******           ***              ***
#   ***      ***         *****           *****              *
#    **      ****         ***           *******            ***
#     *      *****         *          ***********         *****
#   (А)       (Б)         (В)             (Г)              (Д)
#
# *    *      *             *         *****            *
# **  **      **           **         ****            **
# ******      ***         ***         ***            ***
# **  **      **           **         **            ****
# *    *      *             *         *            *****
#   (Е)       (Ж)          (З)       (И)             (К)
# ''')
#
# shape = input("Выберите фигуру (от 'А' до 'К'): ")
#
# if 'А' <= shape <= 'К':
#     size = 5
#
#     for i in range(1, size + 1):
#         for j in range(1, size + 1):
#             if shape == 'А' and j >= i:
#                 print("*", end="")
#             elif shape == 'Б' and j <= i:
#                 print("*", end="")
#             elif shape == 'В' and j >= i and i + j <= size + 1:
#                 print("*", end="")
#             elif shape == 'Г' and j <= i and i + j >= size + 1:
#                 print("*", end="")
#             elif shape == 'Д' and ((j >= i and i + j <= size + 1) or (j <= i and i + j >= size + 1)):
#                 print("*", end="")
#             elif shape == 'Е' and ((j <= i and i + j <= size + 1) or (j >= i and i + j >= size + 1)):
#                 print("*", end="")
#             elif shape == 'Ж' and j <= i and i + j <= size + 1:
#                 print("*", end="")
#             elif shape == 'З' and j >= i and i + j >= size + 1:
#                 print("*", end="")
#             elif shape == 'И' and j + i <= size + 1:
#                 print("*", end="")
#             elif shape == 'К' and j + i >= size + 1:
#                 print("*", end="")
#             else:
#                 print(" ", end='')
#         print()
# else:
#     print("Неправильный выбор!")















