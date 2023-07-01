# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.


class Rectangle:
    def __init__(self, length, width=None):
        """Метод для создания инициализации экземпляра прямоугольника."""
        self.length = length
        self.width = width if width is not None else length

    def area(self):
        """Метод для вычисления площади прямоугольника."""
        return self.length * self.width

    def perimeter(self):
        """Метод для вычисления периметра прямоугольника."""
        return 2 * (self.length + self.width)

    def __add__(self, other):
        """Метод для сложения прямоугольников."""
        new_perimeter = self.perimeter() + other.perimeter()
        new_a = self.length
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __sub__(self, other):
        """Метод для вычитания прямоугольников."""
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_a = min(self.length, self.width, other.length, other.width)
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __str__(self):
        """Метод для вывода прямоугольника на печать."""
        return f'Прямоугольник {self.length}х{self.width}'


if __name__ == '__main__':
    r1 = Rectangle(10, 20)
    r2 = Rectangle(10)
    print(f'{r1.area()}, {r1.perimeter()}')
    print(f'{r2.area()}, {r2.perimeter()}')
    res_sum = r1 + r2
    print(res_sum.length, res_sum.width)
    res_sub = r1 - r2
    print(res_sub.length, res_sub.width)
