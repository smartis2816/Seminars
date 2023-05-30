# Напишите функцию принимающую на вход только ключевые параметры и
# возвращающую словарь, где ключ - значение переданного аргумента,
# а значение - имя аргумента. Если ключ не хешируем, используйте
# его строковое представление.

import typing


def task_2(**kwargs):
    result = dict()
    for key, value in kwargs.items():
        if not isinstance(value, typing.Hashable):
            value = str(value)
        result.setdefault(value, key)
    return result


print(task_2(key_1=87, key_2='text', key_3=[5, 3, 1]))
