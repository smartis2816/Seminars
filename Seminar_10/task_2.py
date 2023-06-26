# Задание №2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width is not None else length

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


if __name__ == '__main__':
    r1 = Rectangle(10, 20)
    r2 = Rectangle(10)
    print(f'{r1.area()}, {r1.perimeter()}')
    print(f'{r2.area()}, {r2.perimeter()}')
