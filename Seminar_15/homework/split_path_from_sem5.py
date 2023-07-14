# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

# Напишите функцию, которая принимает на вход строку -
# абсолютный путь до файла. Функция возвращает кортеж из
# трёх элементов: путь, имя файла, расширение файла.

import logging
import os.path
import sys

MY_PATH = r"C:\Program Files\JetBrains\PyCharm Community Edition 2022.3.2\bin\pycharm64.exe"

FORMAT = '{levelname} - {asctime} - Функция {funcName} записала сообщение: {message}'
logging.basicConfig(format=FORMAT, style='{', filename='info.log', level=logging.INFO, encoding='UTF-8')
logger = logging.getLogger(__name__)


def split_path(file_path: str) -> tuple:
    try:
        path, file = os.path.split(file_path)
        name, extension = file.split('.')
        logger.info(f'Абсолютный путь успешно разделён на путь - {path}, '
                    f'имя файла - {name}, расширение файла - {extension}')
        return path, name, extension
    except TypeError:
        logging.error('Переданный путь не является строкой')
    except ValueError:
        logging.error('Передан невалидный путь')


if __name__ == '__main__':
    # print(split_path(MY_PATH))
    split_path(sys.argv[1])
