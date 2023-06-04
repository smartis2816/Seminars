# Создайте функцию генератор чисел Фибоначчи


def task_3():
    prev = 0
    cur = 1
    while True:
        yield cur
        prev, cur = cur, prev + cur


fibonacci = task_3()
for _ in range(26):
    print(next(fibonacci), end=' ')
