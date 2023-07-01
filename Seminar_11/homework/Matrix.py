# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц


class Matrix:
    def __init__(self, matrix: tuple, rows: int, cols: int):
        """Метод для инициализации матрицы."""
        self.matrix = matrix
        self.rows = rows
        self.cols = cols

    def __str__(self):
        """Метод для вывода матрицы на печать."""
        return str(self.matrix)

    def __eq__(self, other):
        """Метод для сравнения матриц."""
        return all((i == j for i, j in zip(self.matrix, other.matrix)))

    def __add__(self, other):
        """Метод для сложения матриц."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Размеры матриц не совпадают')
        else:
            result = tuple([self.matrix[i][j] + other.matrix[i][j]
                            for j in range(len(self.matrix[0]))] for i in range(len(other.matrix)))
            return Matrix(result, self.rows, self.cols)

    def __mul__(self, other):
        """Метод для умножения матриц."""
        if self.cols == other.rows:
            result = [[0 for row in range(len(other.matrix[0]))] for col in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    for k in range(len(self.matrix[0])):
                        result[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(tuple(result), self.rows, other.cols)
        else:
            raise ValueError('Размеры матриц не совместимы для умножения')


if __name__ == '__main__':
    m1 = Matrix(((0, 5, 9), (8, 4, 1), (2, 6, 7)), 3, 3)
    m2 = Matrix(((0, 5, 9), (8, 4, 1), (2, 6, 7)), 3, 3)
    m3 = Matrix(((10, 9, 1), (6, 4, 2), (4, 3, 8)), 3, 3)
    print(m1)
    print(m2)
    print(m3)
    print('==================================')
    print(f'm1 == m2? {m1 == m2}')
    print(f'm1 == m3? {m1 == m3}')
    print(f'm2 == m3? {m2 == m3}')
    print('==================================')
    print(f'm1 + m2 = {m1 + m2}')
    print(f'm1 + m3 = {m1 + m3}')
    print(f'm2 + m3 = {m2 + m3}')
    print('==================================')
    print(f'm1 * m2 = {m1 * m2}')
    print(f'm1 * m3 = {m1 * m3}')
    print(f'm2 * m3 = {m2 * m3}')
