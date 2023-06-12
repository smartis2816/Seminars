from random import choice, randint

# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.


VOWELS = 'aoeiuy'
CONSONATS = 'bcdfghjklmnpqrstvwxyz'


def gen_files(extension: str, min_len_name: int = 6, max_len_name: int = 30, min_len_byte: int = 256,
              max_len_byte: int = 4096, count_files: int = 42):
    for _ in range(count_files):
        name = ''.join(choice(VOWELS) if i % 3 == 0 else choice(CONSONATS)
                       for i in range(randint(min_len_name, max_len_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_len_name, max_len_name)))
        with open(f'{name}.{extension}', 'wb') as f:
            f.write(data)












