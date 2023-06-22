import random
from typing import Callable


# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.


def decor(func: Callable):
    MAX_COUNT = 10
    MAX_NUM = 100
    MIN_COUNT = 1
    MIN_NUM = 1

    def wrapper(*args, **kwargs):
        input_count, input_num = args
        if MIN_COUNT > input_count or input_count > MAX_COUNT:
            input_count = random.randint(MIN_COUNT, MAX_COUNT)
        if MIN_NUM > input_num or input_num > MAX_NUM:
            input_num = random.randint(MIN_NUM, MAX_NUM)
        return func(input_count, input_num)

    return wrapper


@decor
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
    res = two_nums(11, 20)

