
# Задание №5
# � Добавьте в модуль с загадками функцию, которая хранит
# словарь списков.
# � Ключ словаря - загадка, значение - список с отгадками.
# � Функция в цикле вызывает загадывающую функцию, чтобы
# передать ей все свои загадки.

import task_4


_ANSWERS = dict()


def task_5():
    my_dict = {
        'Не лает, не кусает, в дом не пускает': ['замок', 'замочек', 'засов'],
        'Деревянный брусок, а на нем растет лесок': ['щётка', 'щетка'],
        'В лесу без огня котел кипит': ['муравейник', 'Муравейник']
    }
    for key, value in my_dict.items():
        task_4.task_4(key, value, 3)
    return None









