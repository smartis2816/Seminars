
# Напишите однострочный генератор словаря, который
# принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием
# процентов вида “10.25%”. В результате получаем
# словарь с именем в качестве ключа и суммой премии
# в качестве значения. Сумма рассчитывается как
# ставка умноженная на процент премии.


def task_2(names: list[str], rates: list[int], bonuses: list[str]) -> dict:
    return {name: rate * (float(bonus.replace('%', '')) / 100)
            for name, rate, bonus in zip(names, rates, bonuses)}


names = ['Sheldon', 'Leonard', 'Rajesh', 'Howard']
rates = [75000, 67540, 59870, 55780]
bonuses = ['15.25%', '13.50%', '10.25%', '11.90%']

print(task_2(names, rates, bonuses))













