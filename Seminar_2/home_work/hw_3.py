
# Задание, которое пропустили на семинаре
# Задание №5
# ✔ Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.

import cmath

a = complex(input('Введите коэффициент a: '))
b = complex(input('Введите коэффициент b: '))
c = complex(input('Введите коэффициент c: '))


def solve_task(a: complex, b: complex, c: complex):
    d: complex = b * b - 4 * a * c
    x1: complex = (-b + cmath.sqrt(d)) / (2 * a)
    x2: complex = (-b - cmath.sqrt(d)) / (2 * a)
    print(d, x1, x2)


solve_task(a, b, c)










