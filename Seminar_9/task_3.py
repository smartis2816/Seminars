# Задание №3
# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.
import json
from typing import Callable


def deco(func: Callable) -> Callable:
    with open(f'{func.__name__}.json', 'r') as f:
        final_dict = json.load(f)

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        final_dict.update({str(result): args})
        final_dict.update({**kwargs})
        with open(f'{func.__name__}.json', 'w') as f:
            json.dump(final_dict, f, indent=2)

    return wrapper


@deco
def add(a: int, b: int) -> int:
    return a + b


def multy(a, b, *args, **kwargs):
    return a * b

if __name__ == '__main__':
    multy(2, 3)
