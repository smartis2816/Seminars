# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого
# отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше
# суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить
# является ли треугольник разносторонним, равнобедренным или равносторонним.


print('Необходимо ввести длины 3-х сторон треугольника.')
a = input('Длина стороны a: ')
b = input('Длина стороны b: ')
c = input('Длина стороны c: ')

if a == b == c:
    print('Треугольник является равносторонним')
elif a + b > c and a + c > b and b + c > a:
    if a == b or a == c or b == c:
        print('Треугольник является равнобедренным')
    else:
        print('Треугольник существует')
else:
    print('Треугольник не существует')
