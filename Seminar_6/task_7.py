# Задание №7
# � Создайте модуль и напишите в нём функцию, которая
# получает на вход дату в формате DD.MM.YYYY
# � Функция возвращает истину, если дата может существовать
# или ложь, если такая дата невозможна.
# � Для простоты договоримся, что год может быть в диапазоне
# [1, 9999].
# � Весь период (1 января 1 года - 31 декабря 9999 года)
# действует Григорианский календарь.
# � Проверку года на високосность вынести в отдельную
# защищённую функцию.

from datetime import datetime



def _is_leap_year(date: str) -> bool:
    year = int(date.split('.')[-1])
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def check_year(date: str) -> bool:
    try:
        _ = datetime.strptime(date, '%d.%m.%Y').date()
        return True
    except:
        return False


def date_validator(date: str) -> bool:
    if check_year(date):
        if _is_leap_year(date):
            print(f'Год {date.split(".")[-1]} високосный')
        else:
            print(f'Год {date.split(".")[-1]} обычный')
        return True
    else:
        print('Дата заполнена некорректно')
        return False


