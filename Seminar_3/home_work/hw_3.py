# Создайте словарь со списком вещей для похода в качестве ключа и
# их массой в качестве значения. Определите какие вещи влезут в рюкзак
# передав его максимальную грузоподъёмность. Достаточно вернуть один
# допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

from itertools import combinations

BAG_CAPACITY = 10
MINIMUM_NUMBER_OF_THINGS_IN_BAG = 2
things = {'flashlight': 1, 'tent': 5, 'food': 2, 'sleeping bag': 3, 'first aid kit': 2, 'water': 2}


def set_traveling_kit(capacity: int, things: dict) -> dict:
    result = {}
    for k, v in things.items():
        if v <= capacity:
            result.setdefault(k, v)
            capacity -= v
    return result


def set_traveling_kit_comb(capacity: int, things: dict) -> list:
    result = []
    bag_set: int = 2
    while bag_set <= len(things):
        for i in range(len(things) + 1):
            for comb_set in combinations(things.items(), bag_set):
                if sum(j[1] for j in comb_set) <= capacity:
                    result.append(comb_set)
            bag_set += 1
    return result


print(f'Только один вариант комплектации:\n{set_traveling_kit(BAG_CAPACITY, things)}\n')
print('Все варианты комплектации с условием, что берётся минимум 2 вещи:')
print(*set_traveling_kit_comb(BAG_CAPACITY, things), sep="\n")
