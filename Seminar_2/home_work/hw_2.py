import fractions
import math


# Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем. Программа должна возвращать
# сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

def get_fraction():
    a, b = map(int, input('Введите дробь в формате “a/b”: ').split('/'))
    return a, b


def sum_fractions(a1: int, a2: int, b1: int, b2: int) -> str:
    if a2 == b2:
        return ''.join([str(a1 + b1), '/', a2])
    else:
        scm = (a2 * b2) // math.gcd(a2, b2)
        res = a1 * (scm // a2) + b1 * (scm // b2)
        return ''.join([str(res), '/', str(scm)])


def mult_fractions(a1: int, a2: int, b1: int, b2: int) -> str:
    numerator = a1 * b1
    denominator = a2 * b2
    scd = math.gcd(numerator, denominator)
    return ''.join([str(numerator // scd), '/', str(denominator // scd)])


a1, a2 = get_fraction()
b1, b2 = get_fraction()

print(f'Сумма дробей через свою функцию: {sum_fractions(a1, a2, b1, b2)}')
print(f'Произведение дробей через свою функцию: {mult_fractions(a1, a2, b1, b2)}')

c = fractions.Fraction(a1, a2)
d = fractions.Fraction(b1, b2)
print(f'Сумма дробей через встроенную функцию: {c + d}')
print(f'Произведение дробей через встроенную функцию: {c * d}')
