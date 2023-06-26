# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните
# его из класса-фабрики.

from Animals import Bird, Dog, Fish


class AnimalFactory:
    def create_animal(self, animal_type, name, weight, age):
        if animal_type == 'Bird':
            return Bird(name, weight, age, animal_type)
        elif animal_type == 'Dog':
            return Dog(name, weight, age, animal_type)
        elif animal_type == 'Fish':
            return Fish(name, weight, age, animal_type)
        else:
            return None


if __name__ == '__main__':
    animal_factory = AnimalFactory()
    new_animal = animal_factory.create_animal('Bird', 1.5, 3, 'canary')
    print(new_animal)
