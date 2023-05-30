# Задание №1
# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.


# def task_1(text: str) -> None:
#     text_list = sorted(text.split())
#     max_len = len(max(text_list, key=len))
#     for num, item in enumerate(text_list, start=1):
#         print(f'{num}. {item:>{max_len}}')
#
#
# text = 'Вывести функцией каждое слово с новой строки'
# task_1(text)

# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.


# def task_2(text: str):
#     return list(set(ord(i) for i in text))
#
#
# text = 'Напишите функцию, которая принимает строку текста'
# print(*task_2(text), sep=', ')


# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.


# def task_3(input: str) -> dict:
#     numbers = sorted(map(int, input.split()))
#     new_dict = {}
#     for i in numbers:
#         new_dict.setdefault(chr(i), i)
#     return new_dict
#
#
# input = '78 33'
# print(task_3(input))

# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.


# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.


# def task_5(names: list[str], rate: list[int], bonus: list[str]) -> dict[str:float]:
#     res = dict()
#     for i in range(len(names)):
#         res.setdefault(names[i], rate[i] * (float(bonus[i].replace('%', ''))/100))
#     return res
#
#
# names = ['Frodo', 'Sam', 'Aragorn', 'Gandalf', 'Gimli', 'Legolas']
# rate = [400, 350, 500, 840, 620, 620]
# bonus = ['10.25%', '11.05%', '8.30%', '20.10%', '9.48%', '9.48%']
# print(task_5(names, rate, bonus))

# Задание №6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.


# def task_6(numbers: list[int], ind_min: int, ind_max: int) -> int:
#     if ind_min > ind_max:
#         task_6(numbers, ind_max, ind_min)
#     if ind_min < 0:
#         ind_min = 0
#     if ind_max > len(numbers) - 1:
#         ind_max = len(numbers) - 1
#     return sum(numbers[ind_min: ind_max + 1])
#
#
# list_t6 = [4, 6, 9, 1, 7, 3, 4, 5, 11, 5]
# a, b = 2, 5
# print(task_6(list_t6, a, b))


# Задание №7
# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

# def task_7(input: dict[str: list[int | float]]) -> bool:
#     for v in input.values():
#         if sum(v) < 0:
#             return False
#     return True
#
#
# dict_t7 = {'company_1': [50, -35], 'company_2': [45, -25], 'company_3': [74, -48]}
# print(task_7(dict_t7))


# Задание №8
# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

# def task_8():
#     pass




