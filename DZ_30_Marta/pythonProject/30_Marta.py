# 1.
# def gcd(a, b):
#   if b == 0:
#     return abs(a)
#   else:
#     return gcd(b, a % b)
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# gcd_value = gcd(a, b)
#
# print("Наибольший общий делитель:", gcd_value)

# 2.
def is_safe(board, row, col):

    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]): # Проверяем, находится ли клетка за пределами доски.
        return False

    if board[row][col] != 0: # Проверяем, не занята ли клетка другим конем.
        return False

    for i, j in zip([-2, -1, 1, 2, -2, -1, 1, 2], [-1, -2, -2, -1, 1, 2, 2, 1]): # Проверяем, не находится ли клетка под боем другим конем.
        if 0 <= row + i < len(board) and 0 <= col + j < len(board[0]) and board[row + i][col + j] == 1:
            return False

    return True # Клетка безопасна.
def solve_knight_tour(board, row, col, move_num):

    if move_num == len(board) ** 2: # Если номер хода равен количеству клеток на доске, значит задача решена.
        return True

    for i, j in zip([-2, -1, 1, 2, -2, -1, 1, 2], [-1, -2, -2, -1, 1, 2, 2, 1]): # Пробуем все возможные ходы коня из текущей клетки.

        if is_safe(board, row + i, col + j): # Если ход безопасен, делаем его и переходим к следующему ходу.
            board[row + i][col + j] = move_num + 1
            if solve_knight_tour(board, row + i, col + j, move_num + 1):
                return True

            board[row + i][col + j] = 0  # Если ход не привел к решению, отменяем его.


    return False # Если ни один из ходов не привел к решению, возвращаем False.


def print_solution(board):
    for row in board:
        print(' '.join(map(str, row)))

n = 6 # Размер доски

board = [[0 for _ in range(n)] for _ in range(n)] # Создаем шахматную доску

row, col = map(int, input("Введите координаты начальной клетки (строка, столбец): ").split()) # Запрашиваем у пользователя координаты начальной клетки

if solve_knight_tour(board, row, col, 1): # Ход коня
    print("Решение найдено:")
    print_solution(board)
else:
    print("Решение не найдено.")