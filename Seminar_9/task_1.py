from typing import Callable


# Задание №1
# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.


def two_nums(count: int, num: int) -> Callable[[], None]:
    def random_nums():
        for i in range(1, count + 1):
            user_input = input("Введите число от 1 до 100:")
            if int(user_input) == num:
                print(f'Вы угадали с {count} попыток')
        else:
            print(f'Вы не угадали')
    return random_nums


if __name__ == '__main__':
    two_nums(3, 20)()



