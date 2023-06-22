# Задание №5
# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.
from typing import Callable

import task_1 as t1
import task_3 as t3
import task_4 as t4


@t3.deco
@t4.count_of_runs(3)
def two_nums(count: int, num: int) -> Callable[[], None]:
    def random_nums():
        for i in range(1, count + 1):
            user_input = input("Введите число от 1 до 100:")
            if int(user_input) == num:
                print(f'Вы угадали с {count} попыток')
        else:
            print(f'Вы не угадали')

    return random_nums


if __name__ == '__main__':
    two_nums(3, 20)()
