# Напишите функцию для транспонирования матрицы

def transpose_1(matrix):
    return list(zip(*matrix))


def transpose_2(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'Изначальная матрица: {matrix}')
print(f'Транспонированная матрица: {transpose_1(matrix)}')
print(f'Транспонированная матрица: {transpose_2(matrix)}')
