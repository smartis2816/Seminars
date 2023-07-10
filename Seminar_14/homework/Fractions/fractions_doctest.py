# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# ○ doctest,
# ○ unittest,
# ○ pytest.


# Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем. Программа должна возвращать
# сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

import fractions
import math
import doctest


def get_fraction():
    a, b = map(int, input('Введите дробь в формате “a/b”: ').split('/'))
    return a, b


def sum_fractions(a1: int, a2: int, b1: int, b2: int) -> str:
    """
    >>> sum_fractions(3, 4, 7, 8)
    '13/8'
    """
    if a2 == b2:
        return ''.join([str(a1 + b1), '/', a2])
    else:
        scm = (a2 * b2) // math.gcd(a2, b2)
        res = a1 * (scm // a2) + b1 * (scm // b2)
        return ''.join([str(res), '/', str(scm)])


def mult_fractions(a1: int, a2: int, b1: int, b2: int) -> str:
    """
    >>> mult_fractions(3, 4, 7, 8)
    '21/32'
    """
    numerator = a1 * b1
    denominator = a2 * b2
    scd = math.gcd(numerator, denominator)
    return ''.join([str(numerator // scd), '/', str(denominator // scd)])


if __name__ == '__main__':
    # a1, a2 = get_fraction()
    # b1, b2 = get_fraction()
    # print(f'Сумма дробей через свою функцию: {sum_fractions(a1, a2, b1, b2)}')
    # print(f'Произведение дробей через свою функцию: {mult_fractions(a1, a2, b1, b2)}')
    # c = fractions.Fraction(a1, a2)
    # d = fractions.Fraction(b1, b2)
    # print(f'Сумма дробей через встроенную функцию: {c + d}')
    # print(f'Произведение дробей через встроенную функцию: {c * d}')
    doctest.testmod(verbose=True)
