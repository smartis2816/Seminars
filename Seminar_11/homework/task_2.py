# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

# Задание №4
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

class Archive:
    numbers = []
    values = []

    def __new__(cls, number: int, value: str):
        """Переопределение метода __new__ для
        сохранения аргументов в списки."""
        instance = super().__new__(cls)
        cls.numbers.append(number)
        cls.values.append(value)
        return instance

    def __init__(self, number: int, value: str):
        """Метод для создания экземпляра класса."""
        self.number = number
        self.value = value

    def __repr__(self):
        """Метод для вывода на печать экземпляра класса
        для программиста"""
        return f'Archive({self.number}, "{self.value}")'

    def __str__(self):
        """Метод для вывода на печать экземпляра класса
        для пользователя"""
        return f'Archive(number={self.number}, value={self.value})'


if __name__ == '__main__':
    a_1 = Archive(1, 'one')
    a_2 = Archive(2, 'two')
    print(f'{a_1.numbers} {a_1.values}')
    print(f'{a_2.numbers} {a_2.values}')
    a_3 = Archive(3, 'three')
    print(f'{a_3.numbers} {a_3.values}')
    print(a_1.__repr__())
    print(f'{a_1 = }')
    print(a_1)
