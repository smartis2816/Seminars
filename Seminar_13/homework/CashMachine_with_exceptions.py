class CustomException(Exception):
    pass


class CustomInputError(CustomException):
    def __init__(self, value, amount):
        self.value = value
        self.amount = amount

    def __str__(self):
        return f'Сумма {self.value} недопутима.\nСумма должна быть кратна {self.amount} и быть не меньше 1 у.е.'


class NotEnoughMoney(CustomException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'На балансе не хватает средств для снятия такой суммы в размере {self.value} у.е.'


class CashMachine:
    __AMOUNT = 50
    __COMMISSION_PERCENTAGE = 0.015
    __COMMISSION_MIN = 30
    __COMMISSION_MAX = 600
    __BONUS_MULTIPLIER = 1.03
    __TAX = 0.1
    __WEALTH_INDICATOR = 5_000_000

    def __init__(self):
        self.__balance = 0
        self.__operations_counter = 0
        self.__history = []

    def __check_wealth(self):
        if self.__balance > self.__WEALTH_INDICATOR:
            return True
        return False

    def __check_bonus(self):
        self.__operations_counter += 15
        if self.__operations_counter % 3 == 0:
            self.__balance = int(self.__balance * self.__BONUS_MULTIPLIER)
            print(f'Начислен бонус в размере {int((self.__BONUS_MULTIPLIER - 1) * 100)}% от суммы операции.\n')
        return None

    def __check_money(self):
        print(f'Текущий баланс составляет: {self.__balance}\n')

    def show_operations(self):
        if len(self.__history) != 0:
            print(*self.__history, sep='\n')
        else:
            print('История операция пока пустая.')

    def __check_commission(self, operation_sum):
        commission = int(operation_sum * self.__COMMISSION_PERCENTAGE)
        if commission < self.__COMMISSION_MIN:
            commission = self.__COMMISSION_MIN
        elif commission > self.__COMMISSION_MAX:
            commission = self.__COMMISSION_MAX
        return commission

    def __input_sum(self):
        if self.__check_wealth():
            self.__balance = int(self.__balance * 0.9)
        operation_sum = int(
            input(f'\nСумма пополнения и снятия кратны {self.__AMOUNT} у.е. Введите сумму операции: '))
        if not operation_sum % self.__AMOUNT == 0:
            raise CustomInputError(operation_sum, self.__AMOUNT)
        elif int(operation_sum) < 1:
            raise CustomInputError(operation_sum, self.__AMOUNT)
        return operation_sum

    def __add_money(self):
        operation_sum = self.__input_sum()
        self.__balance += operation_sum
        self.__history.append(('replenishment', operation_sum))
        print('\nОперация проведена успешно.')
        self.__check_bonus()
        self.__check_money()
        return None

    def __get_money(self):
        operation_sum = self.__input_sum()
        operation_sum += self.__check_commission(operation_sum)
        if self.__balance >= operation_sum:
            self.__balance -= operation_sum
            self.__history.append(('withdrawal', operation_sum))
            print('\nОперация проведена успешно.')
            self.__check_bonus()
            self.__check_money()
        else:
            raise NotEnoughMoney(operation_sum)
        return None

    def menu(self):
        while True:
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
                    self.__add_money()
                case '2':
                    self.__get_money()
                case '3':
                    self.__check_money()
                case '4':
                    self.show_operations()
                case '5':
                    print('Работа банкомата завершается...')
                    exit()


if __name__ == '__main__':
    cash_machine = CashMachine()
    cash_machine.menu()
