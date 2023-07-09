# Задание №1
# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.


def num_exc():
    while True:
        num = input('Введите целое или вещественное число: ')
        try:
            num = int(num)
            break
        except ValueError as e:
            try:
                num = float(num)
                break
            except ValueError as e:
                print('Введено невалидное значение. Попробуйте снова.')
    return num


if __name__ == '__main__':
    num_exc()
