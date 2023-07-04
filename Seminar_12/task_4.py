# Задание №4
# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# Используйте декораторы свойств.
# Задание №5
# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.


class Rectangle:
    __slots__ = ('_width', '_length')

    def __init__(self, length, width=None):
        """Метод для создания инициализации экземпляра прямоугольника."""
        self._length = length
        self._width = width if width is not None else length

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError(f'{self._width} не может иметь отрицательное значение')

    @length.setter
    def length(self, value):
        if value > 0:
            self._length = value
        else:
            raise ValueError(f'{self._length} не может иметь отрицательное значение')

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
