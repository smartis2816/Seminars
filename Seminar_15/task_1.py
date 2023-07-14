# Задание №1
# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.
import logging

logging.basicConfig(filename='error.log', level=logging.ERROR, encoding='UTF-8', filemode='w')


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError as zd:
        logging.error(f'Вы делите на 0. Ошибка: {zd}')


if __name__ == '__main__':
    division(1, 0)
