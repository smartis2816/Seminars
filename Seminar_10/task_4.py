# Задание №4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь
import random

from task_3 import Person


class Employee(Person):
    def __init__(self, profession, firstname, lastname, age, gender):
        super().__init__(firstname, lastname, age, gender)
        self.employee_id = self._gen_number()
        self.secure_level = self._secure_level()
        self.profession = profession

    def _gen_number(self):
        MIN_NUM = 100000
        MAX_NUM = 1000000
        return random.randint(MIN_NUM, MAX_NUM)

    def _secure_level(self):
        sec_id = self._gen_number()
        LEVEL_NUM = 7
        level_num = 0
        while sec_id > 0:
            last_num = sec_id % 10
            level_num += last_num
            sec_id /= 10
        return level_num % LEVEL_NUM

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.employee_id} - {self.secure_level} - {self.profession}"


if __name__ == '__main__':
    employee_1 = Employee('Программист', 'Иван', 'Иванов', 25, 'мужской')
    print(employee_1)
