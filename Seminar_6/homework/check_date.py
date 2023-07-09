from sys import argv
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


if __name__ == '__main__':
    date_validator(argv[1])
