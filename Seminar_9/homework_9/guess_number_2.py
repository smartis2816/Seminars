# Задание №2
# � Создайте модуль с функцией внутри.
# � Функция принимает на вход три целых числа: нижнюю и
# верхнюю границу и количество попыток.
# � Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число
# попыток.
# � Функция выводит подсказки “больше” и “меньше”.
# � Если число угадано, возвращается истина, а если попытки
# исчерпаны - ложь.

import random


def task_2(lower=1, upper=10, attempts=3):
    number = random.randint(lower, upper + 1)
    while attempts != 0:
        attempt = int(input(f'Угадайте число от {lower} до {upper} за {attempts} попыток: '))
        if attempt > number:
            print(f"Загаданное число меньше {attempt}.")
            attempts -= 1
            print(f"Осталось {attempts} попыток.")
        elif attempt < number:
            print(f"Загаданное число больше {attempt}.")
            attempts -= 1
            print(f"Осталось {attempts} попыток.")
        else:
            print(f"Вы угадали! Это число {number}")
            return True
    print(f"Попытки закончились, и Вы не смогли угадать число - {number}.")
    return False
