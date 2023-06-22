# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.
import csv
import json
import math
import random

MIN_COUNT_OF_ROWS = 100
MAX_COUNT_OF_ROWS = 1000


def csv_generator():
    my_list = [(random.randint(1, 101), random.randint(1, 101), random.randint(1, 101)) for _ in
               range(random.randint(MIN_COUNT_OF_ROWS, MAX_COUNT_OF_ROWS + 1))]
    with open("random_numbers.csv", 'w', newline='', encoding='utf-8') as f:
        wr = csv.writer(f)
        for el in my_list:
            wr.writerow(el)


def calc_from_csv(func):
    def wrapper(*args, **kwargs):
        with open("random_numbers.csv", 'r', newline='', encoding='utf-8') as f:
            return [func(*map(int, row)) for row in csv.reader(f)]

    return wrapper


def saver_to_json(func):
    def wrapper():
        with (open("result.json", 'w', newline='', encoding='utf-8') as f_1,
              open("random_numbers.csv", 'r', encoding='utf-8') as f_2):
            abc_list = [row for row in csv.reader(f_2)]
            result = [{'a': el[0][0], 'b': el[0][1], 'c': el[0][2], 'Решение': el[1]}
                      for el in zip(abc_list, func())]
            json.dump(result, f_1, ensure_ascii=False, indent=2)

    return wrapper


@saver_to_json
@calc_from_csv
def quadratic_roots(a, b, c):
    discriminant = b * b - 4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return [x1, x2]
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        return None


if __name__ == '__main__':
    csv_generator()
    quadratic_roots()

