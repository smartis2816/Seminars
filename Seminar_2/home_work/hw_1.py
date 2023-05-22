# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


def my_hex(num: int) -> str:
    symbols = '0123456789abcdef'
    result = ''
    divider: int = 16
    while num > 0:
        result += symbols[num % divider]
        num //= divider
    return result[::-1]


number: int = int(input('Введите число, которое нужно перевести в 16-тиричную систему: '))
print(f'Результат работы функции my_hex: {my_hex(number)}')
print(f'Результат работы функции hex: {hex(number)}')
