# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции - функции.
# Дополнительно сохраняйте все операции поступления
# и снятия средств в список.

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


AMOUNT = 50
COMMISSION_PERCENTAGE = 0.015
COMMISSION_MIN = 30
COMMISSION_MAX = 600
BONUS_MULTIPLIER = 1.03
TAX = 0.1
WEALTH_INDICATOR = 5_000_000
history_of_operations = []
operations_counter = 0
balance = 0


def input_sum():
    global balance
    if check_wealth():
        balance = int(balance * 0.9)
    while True:
        operation_sum = int(input(f'\nСумма пополнения и снятия кратны {AMOUNT} у.е. Введите сумму операции: '))
        if not operation_sum % AMOUNT == 0:
            print(f'\nНедопустимая сумма. Попробуйте ещё раз.')
            continue
        elif int(operation_sum) < 1:
            print(f'\nНедопустимая сумма. Сумма пополнения и снятия не должны быть меньше 1 у.е.')
            continue
        else:
            break
    return operation_sum


def add_money():
    global balance
    global history_of_operations
    operation_sum = input_sum()
    balance += operation_sum
    history_of_operations.append(('replenishment', operation_sum))
    print('\nОперация проведена успешно.')
    check_bonus()
    check_money()
    return None


def get_money():
    global balance
    global history_of_operations
    operation_sum = input_sum()
    operation_sum += check_commission(operation_sum)
    if balance >= operation_sum:
        balance -= operation_sum
        history_of_operations.append(('withdrawal', operation_sum))
        print('\nОперация проведена успешно.')
        check_bonus()
        check_money()
    else:
        print('На балансе не хватает средств для снятия такой суммы.\n')
    return None


def check_commission(operation_sum):
    commission = int(operation_sum * COMMISSION_PERCENTAGE)
    if commission < COMMISSION_MIN:
        commission = COMMISSION_MIN
    elif commission > COMMISSION_MAX:
        commission = COMMISSION_MAX
    return commission


def check_wealth():
    global balance
    if balance > WEALTH_INDICATOR:
        return True
    return False


def check_bonus():
    global operations_counter
    global balance
    operations_counter += 1
    if operations_counter % 3 == 0:
        balance = int(balance * BONUS_MULTIPLIER)
        print(f'Начислен бонус в размере {int((BONUS_MULTIPLIER - 1) * 100)}% от суммы операции.\n')
    return None


def check_money():
    global balance
    print(f'Текущий баланс составляет: {balance}\n')


def show_operations():
    global history_of_operations
    if len(history_of_operations) != 0:
        print(*history_of_operations, sep='\n')
    else:
        print('История операция пока пустая.')


def menu():
    print("""\nДоступные действия: 
    1) пополнить счёт
    2) снять наличные
    3) узнать текущую сумму на счету
    4) посмотреть историю операций
    5) выйти
    Введите номер желаемого действия. 
    """)
    match input():
        case '1':
            add_money()
        case '2':
            get_money()
        case '3':
            check_money()
        case '4':
            show_operations()
        case '5':
            print('Работа банкомата завершается...')
            exit()


while True:
    menu()
