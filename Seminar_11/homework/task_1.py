# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
import time


class MyString(str):
    def __new__(cls, value: str, name: str):
        """Расширяем класс String:
        дополнительно хранятся имя автора строки и время создания"""
        instance = super().__new__(cls, value)
        instance.value = value
        instance.name = name
        instance.created_at = time.time()
        return instance

    def __str__(self):
        """Переопределение метода __str__ в классе String
        для вывода на печать экзеипляра класса MyString"""
        return self.value


if __name__ == "__main__":
    my_string = MyString('тЕст', 'доп. аргумент')
    print(my_string)
    print(my_string.name)
    print(my_string.created_at)
    print(my_string.upper())

