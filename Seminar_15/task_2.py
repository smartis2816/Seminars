# Задание №2
# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.

# Задание №3
# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.

from typing import Callable
import logging

FORMAT = '{levelname} - {asctime} - {funcName}: {message}'
logging.basicConfig(format=FORMAT, style='{', filename='info.log', level=logging.INFO, encoding='UTF-8', filemode='a')
logger = logging.getLogger(__name__)


def deco_logger(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        a, b = args
        res = func(a, b)
        logger.info(f' {func.__name__} {a} * {b} = {res} ')

    return wrapper


@deco_logger
def add(a: int, b: int) -> int:
    return a + b


@deco_logger
def multy(a, b, *args, **kwargs):
    return a * b


if __name__ == '__main__':
    multy(2, 7)
