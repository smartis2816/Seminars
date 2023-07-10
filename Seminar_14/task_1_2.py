# Задание №1
# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

# Задание №2
# Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)


import string
import doctest


def remove_chars(text: str) -> str:
    """
    >>> remove_chars('dfdfhdfh wreg')
    'dfdfhdfh wreg'
    >>> remove_chars('dFDfhdfh WREG')
    'dfdfhdfh wreg'
    >>> remove_chars('bg!&&,.j j:;')
    'bgj j'
    >>> remove_chars('валджьЬОП')
    ''
    >>> remove_chars('dfkLLLLmbn ;!ICL роивмghv;!!!')
    'dfkllllmbn icl ghv'
    """
    alpha = string.ascii_letters + ' '
    result = text
    for t in text:
        if t not in alpha:
            result = result.replace(t, '')
    return result.lower()


if __name__ == '__main__':
    # print(remove_chars('dfsBKdjnb апвыривтп2462'))
    doctest.testmod(verbose=True)
