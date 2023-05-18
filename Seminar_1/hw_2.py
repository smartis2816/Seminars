# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на
# единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

LOWER_BOUND = 2
UPPER_BOUND = 100_000


def get_number():
    while True:
        print('Задайте число, которое больше 1 и меньше 100 тысяч')
        num = int(input('Введите число: '))
        if LOWER_BOUND <= num < UPPER_BOUND:
            break
        else:
            print('Вы ввели неверное число')
            continue
    return num


def check_num(num):
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True


if check_num(get_number()):
    print('Вы ввели простое число')
else:
    print('Вы ввели составное число')
