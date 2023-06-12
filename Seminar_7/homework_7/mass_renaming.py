
# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из
# исходного имени файла. К ним прибавляется желаемое конечное имя,
# если оно передано. Далее счётчик файлов и расширение.

from pathlib import Path


def rename_file(target_name: str = 'file', count: int = 1,
                digits_in_count: int = 3, origin_extension: str = '.txt',
                target_extension: str = '.txt', range_of_name: tuple = (0, 0)):
    p = Path(Path().cwd())
    for obj in p.iterdir():
        if obj.suffix == origin_extension:
            obj.rename(''.join(f'{obj.name[range_of_name[0]:range_of_name[1]]}'
                               f'{target_name}{str(count).zfill(digits_in_count)}'
                               f'{target_extension}'))
            count += 1

