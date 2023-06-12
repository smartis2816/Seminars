# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from pathlib import Path
from random import randint, choice

VOWELS = 'aoeiuy'
CONSONATS = 'bcdfghjklmnpqrstvwxyz'


def gen_names(count, str_len_min, str_len_max, file_2: Path):
    with open(file_2, 'a', encoding='utf-8') as f:
        for _ in range(count):
            rad_string = ''.join(choice(VOWELS) if i % 3 == 0 else choice(CONSONATS)
                                 for i in range(randint(str_len_min, str_len_max)))
            f.write(f'{rad_string.capitalize()}\n')
