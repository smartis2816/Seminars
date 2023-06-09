
# Задание №4
# � Создайте модуль с функцией внутри.
# � Функция получает на вход загадку, список с возможными
# вариантами отгадок и количество попыток на угадывание.
# � Программа возвращает номер попытки, с которой была
# отгадана загадка или ноль, если попытки исчерпаны.


def task_4(riddle: str, solutions: list[str], attempts: int) -> int:
    print(riddle)
    count = 1
    while attempts != 0:
        answer = input('Ваш ответ: ')
        if answer in solutions:
            print(f'Верный ответ. Загадка отгадана с {count} попытки.')
            return count
        else:
            attempts -= 1
            print(f'Ответ неверный. Оставшихся попыток - {attempts} ')
            count += 1
    return 0








