# Задание №3
# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.


class Person:
    def __init__(self, firstname, lastname, age, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.__age = age
        self.gender = gender

    def full_name(self):
        return f'{self.firstname} {self.lastname}'

    def get_age(self):
        return self.__age

    def birthday(self):
        self.__age += 1
        return self.__age


if __name__ == '__main__':
    person = Person('Карл', 'Карлов', 20, 'мужской')
    print(person.full_name())
    print(person.get_age())
    print(person.birthday())
    print(person.get_age())

