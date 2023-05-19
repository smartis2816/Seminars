# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(num)

print('Программа загадала целое число в промежутке от 0 до 1000. Попробуйте его угадать за 10 попыток.')

top = UPPER_LIMIT
bottom = LOWER_LIMIT

# Угадывает пользователь
# for i in range(1, 11):
#     print('Попытка № ', i)
#     attempt = int(input('Введите целое число: '))
#     if num == attempt:
#         print('Вы угадали. Это число', attempt)
#         break
#     elif num > attempt:
#         bottom = attempt + 1
#         print('Загаданное число больше ', attempt)
#         print('Теперь вы можете рассматривать диапазон от', bottom, 'до', top)
#     elif num < attempt:
#         top = attempt - 1
#         print('Загаданное число меньше ', attempt)
#         print('Теперь вы можете рассматривать диапазон от', bottom, 'до', top)

# Угадывает компьютер
for i in range(1, 11):
    print('Попытка № ', i)
    attempt = (bottom + top) // 2
    print('Предполагаемое число -', attempt)
    if num == attempt:
        print('Вы угадали. Это число', attempt)
        break
    elif num > attempt:
        bottom = attempt + 1
        print('Загаданное число больше ', attempt)
        print('Теперь вы можете рассматривать диапазон от', bottom, 'до', top)
    elif num < attempt:
        top = attempt - 1
        print('Загаданное число меньше ', attempt)
        print('Теперь вы можете рассматривать диапазон от', bottom, 'до', top)
