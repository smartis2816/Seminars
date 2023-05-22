# Задание №1
# Создайте несколько переменных разных типов.
# Проверьте к какому типу относятся созданные переменные.

# a = 7
# b = 'str'
# c = 3.2 * 1.2 / 1.1
# print(a, b, c, sep='\n')
# print(type(a), type(b), type(c), sep='\n')
# print(f'a - {type(a)}, b - {type(b)}, c - {type(c)}')

# Задание №2
# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

# data = [7, 'str', 3.2 * 1.2 / 1.1, 'str']
# print(data)
# for i, el in enumerate(data, start=1):
#     print(i, el, id(el), el.__sizeof__(), hash(el))
#     if isinstance(el, int):
#         print('Число целое')
#     elif isinstance(el, str):
#         print('Это строка')


# Задание №3
# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

# def task_3(num: int, mode: str) -> str:
#     result = ''
#     convert: int = 2
#     match mode:
#         case 'bin':
#             convert = 2
#         case 'oct':
#             convert = 8
#     while num >= 1:
#         res = num % convert
#         result += str(res)
#         num //= convert
#     return result[::-1]
#
#
# print(task_3(10, 'bin'), f'result: {bin(10)}')
# print(task_3(10, 'oct'), f'result: {oct(10)}')

# Задание №4
# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

# import math as M
# import decimal
#
# DIAMETER: float = 10
#
#
# def calc_s(d):
#     decimal.getcontext().prec = 42
#     return decimal.Decimal(M.pi * M.pow(d / 2, 2))
#
#
# def calc_length_circle(d):
#     decimal.getcontext().prec = 42
#     return decimal.Decimal(M.pi * d)
#
#
# print(calc_s(DIAMETER))
# print(calc_length_circle(DIAMETER))

# Задание №5
# ✔ Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.

# import cmath
#
# a = complex(input('Введите коэффициент a: '))
# b = complex(input('Введите коэффициент b: '))
# c = complex(input('Введите коэффициент c: '))
#
#
# def solve_task(a: complex, b: complex, c: complex):
#     d: complex = b * b - 4 * a * c
#     x_1: complex = (-b + cmath.sqrt(d)) / (2 * a)
#     x_2: complex = (-b - cmath.sqrt(d)) / (2 * a)
#     print(d, x_1, x_2)
#
#
# solve_task(a, b, c)


# Задание №6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

class Bank:
    _BALANCE = 0
    _MIN = 50
    _COMMISSION = 0.015
    _BONUS = 0.03
    _TAX = 0.1
    _OPERATION: int

    def __init__(self):
        self._OPERATION = 0

    def _in(self, cash: int) -> tuple[int, int] or None:
        if cash % self._MIN == 0:
            self._BALANCE += cash
            self._OPERATION += 1
            return self._BALANCE, self._OPERATION
        else:
            return None

    def _out(self, cash: int, commission: int) -> tuple[int, int] or None:
        if cash % self._MIN == 0 and self._BALANCE > 0 and self._BALANCE - (cash + commission) >= 0:
            self._BALANCE -= cash
            self._OPERATION += 1
            return self._BALANCE, self._OPERATION
        else:
            return None

    def _exit(self):
        return 'Работа программы завершается...'

    def _check_commission(self, cash: int) -> int:
        sum_commission = cash * self._COMMISSION
        _MAX = 600
        _MIN = 30

        if sum_commission > _MAX:
            return _MAX
        elif sum_commission < _MIN:
            return _MIN
        else:
            return int(sum_commission)

    def _check_operation(self):
        return (False, True)[self._OPERATION % 3]

    def start(self, mode: str, cash: int = 0) -> str:
        chop = self._check_commission(cash)
        if chop:
            self._BALANCE += self._BALANCE * self._BONUS
        match mode:
            case 'in':
                data = self._in(cash=cash)
                com_data = self._check_commission(cash=cash)
                return f'Средства зачислены. Сумма: {cash}, баланс: {self._BALANCE}'

            case 'out':
                com_data = self._check_commission(cash=cash)
                data = self._out(cash=cash, commission=com_data)
                if data:
                    return f'Операция прошла успешно. Сумма:{cash}, комиссия:{com_data}, баланс:{self._BALANCE}'
                else:
                    return 'Не хватает средств'

            case 'exit':
                return self._exit()


client = Bank()
print(client.start(mode='in', cash=100))
