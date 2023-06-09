# Задание №1
# ✔ Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
#  хранятся в кортеже как значения второго ключа.


# def task_1(text: str) -> dict[int:int]:
#     first, second, third, *others = (int(i) for i in text.split('/'))
#     return {second: first, third: tuple(others)}
#
#
# text = '1/2/3/4/5/6/4/8/9'
# print(task_1(text))


# Задание №2
# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.
# Задание №3
# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

# def task_2(text: str) -> dict[str:int]:
#     return {i: ord(i) for i in text}


# def task_2_2(text: str) -> dict[str:int]:
#     res_iter = iter({k: ord(k) for k in text}.items())
#     print(next(res_iter))
#     print(next(res_iter))
#     print(next(res_iter))
#     print(next(res_iter))
#
#
# text = 'Самостоятельно сохраните в переменной строку текста'
# my_dict = task_2(text)
# print(my_dict)
# task_2_2(text)


# Задание №4
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку


# def task_3():
#     return (i for i in range(0, 101, 2) if i // 10 + i % 10 != 8)
#
#
# for i in task_3():
#     print(i)


# Задание №5
# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

# print(*('FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i for i in range(1, 101)),
#       sep=', ')


# Задание №6
# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.

# LOWER_LIMIT = 2
# UPPER_LIMIT = 10
# COLUMN = 4
#
#
# def task_6():
#     for i in range(LOWER_LIMIT, UPPER_LIMIT, COLUMN):
#         for j in range(LOWER_LIMIT, UPPER_LIMIT + 1):
#             for k in range(i, i + COLUMN):
#                 if j == UPPER_LIMIT and k == i + COLUMN - 1:
#                     print(f'{k:>} x {j:>2} = {k * j:>}\n\n', end='')
#                 elif k == i + COLUMN - 1:
#                     print(f'{k:>} x {j:>2} = {k * j:>}\n', end='')
#                 else:
#                     print(f'{k:>} x {j:>2} = {k * j:>}\t\t', end='')
#
#
# def task_6_2():
#     print(' ', end='')
#     print(*(f'{k:>} x {j:>2} = {k * j:>2}\n\n' if j == UPPER_LIMIT and k == i + COLUMN - 1 else \
#             f'{k:>} x {j:>2} = {k * j:>2}\n' if k == i + COLUMN - 1 else \
#             f'{k:>} x {j:>2} = {k * j:>2}\t\t' \
#             for i in range(LOWER_LIMIT, UPPER_LIMIT, COLUMN)
#             for j in range(LOWER_LIMIT, UPPER_LIMIT + 1)
#             for k in range(i, i + COLUMN)))
#
#
# task_6()
# task_6_2()


# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».









