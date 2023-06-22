# Задание №4
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.
from typing import Callable


def count_of_runs(params: int):
    def decorator(func: Callable):
        my_list = []

        def wrapper(*args, **kwargs):
            for i in range(params):
                result = func(*args, **kwargs)
                my_list.append(result)
            return my_list

        return wrapper

    return decorator


@count_of_runs(3)
def fact(number):
    res = 1
    for i in range(1, number + 1):
        res *= i
    return res


if __name__ == '__main__':
    print(fact(5))
