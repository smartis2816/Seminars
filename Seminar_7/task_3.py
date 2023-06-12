from pathlib import Path
from typing import TextIO


# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.


def _read_or_begin(fd: TextIO) -> str:
    line = fd.readline()
    if not line:
        fd.seek(0)
        return  _read_or_begin(fd)
    return line[:-1]


def combine_files(numbers, names, result):
    with (open(numbers, 'r', encoding='utf-8') as f_num,
          open(names, 'r', encoding='utf-8') as f_words,
          open(result, 'w', encoding='utf-8') as f_res):
        len_nums = sum(1 for _ in f_num)
        len_words = sum(1 for _ in f_words)
        for _ in range(max(len_nums, len_words)):
            num = _read_or_begin(f_num)
            word = _read_or_begin(f_words)
            num_a, num_b = num.split('|')
            mult = int(num_a) * float(num_b)
            if mult < 0:
                f_res.write(f'{word.lower()}{abs(mult)}\n')
            elif mult > 0:
                f_res.write(f'{word.upper()}{round(mult)}\n')



