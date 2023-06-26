# Задание №5
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.
# Задание №6
# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.


class Animal:
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age

    def move(self):
        pass

    def say(self):
        pass

    def __str__(self):
        return f'{self.name} {self.weight} {self.age}'


class Bird(Animal):
    def __init__(self, name, weight, age, bird_type):
        super().__init__(name, weight, age)
        self.bird_type = bird_type

    def move(self):
        print(f'{self.name} flying')

    def say(self):
        print(f'{self.name} sings')

    def __str__(self):
        return f'{super().__str__()} {self.bird_type}'


class Dog(Animal):
    def __init__(self, name, weight, age, dog_type):
        super().__init__(name, weight, age)
        self.dog_type = dog_type

    def move(self):
        print(f'{self.name} running')

    def say(self):
        print(f'{self.name} barks')

    def __str__(self):
        return f'{super().__str__()} {self.dog_type}'


class Fish(Animal):
    def __init__(self, name, weight, age, fish_type):
        super().__init__(name, weight, age)
        self.fish_type = fish_type

    def move(self):
        print(f'{self.name} swimming')

    def say(self):
        print(f'{self.name} silent')

    def __str__(self):
        return f'{super().__str__()} {self.fish_type}'


if __name__ == '__main__':
    bird = Bird('Bird', 1, 2, 'parrot')
    dog = Dog('Dog', 10, 1, 'spaniel')
    fish = Fish('Fish', 2, 1, 'sturgeon')
    print(bird, dog, fish, sep='\n')
