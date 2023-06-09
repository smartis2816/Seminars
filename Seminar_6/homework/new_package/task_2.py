# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутриу него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей
# на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число
# от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга
# верните истину, а если бьют - ложь.

# Напишите функцию в шахматный модуль. Используйте генератор
# случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите
# 4 успешных расстановки.

import random

SIZE = 8
QUANTITY = 4
example = ((0, 5), (1, 3), (2, 6), (3, 0), (4, 7), (5, 1), (6, 4), (7, 2))
board = [[0] * SIZE for _ in range(SIZE)]


def set_random_queens():
    rows = list(range(SIZE))
    columns = list(range(SIZE))
    random.shuffle(rows)
    random.shuffle(columns)
    return tuple(zip(rows, columns))


def get_placement(quantity):
    result = list()
    while quantity > 0:
        attempt = set_random_queens()
        if check_queens(attempt):
            quantity -= 1
            result.append(attempt)
    return result


def check_queens(queens_coordinates):
    global board
    global SIZE
    for row, column in queens_coordinates:
        if board[row][column] == 1:
            return False
        else:
            for i in range(SIZE):
                for j in range(SIZE):
                    if i == row or j == column or row - column == i - j or row + column == i + j:
                        board[i][j] = 1
    return True


if __name__ == '__main__':
    if check_queens(example):
        print('Ферзи не бьют друг друга')
    else:
        print('Есть ферзи, бьющие друг друга')

    queens = get_placement(QUANTITY)
    print(*queens, sep="\n")
