# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.
import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def circumference_length(self):
        return 2 * self.radius * math.pi

    def area(self):
        return math.pi * self.radius ** 2


if __name__ == '__main__':
    circle = Circle(radius=5)
    print(f'{circle.circumference_length()}\n{circle.area()}')
