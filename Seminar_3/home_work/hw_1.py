# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [2, 3, 2, 6, 4, 3, 9, 7, 5, 7]
print(my_list)

new_list = list(set(i for i in my_list if my_list.count(i) > 1))

print(new_list)
