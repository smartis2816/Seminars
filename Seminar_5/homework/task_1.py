# Напишите функцию, которая принимает на вход строку -
# абсолютный путь до файла. Функция возвращает кортеж из
# трёх элементов: путь, имя файла, расширение файла.

import os.path


def task_1(file_path: str) -> tuple:
    path, file = os.path.split(file_path)
    name, extension = file.split('.')
    return path, name, extension


my_path = r"C:\Program Files\JetBrains\PyCharm Community Edition 2022.3.2\bin\pycharm64.exe"
print(task_1(my_path))

