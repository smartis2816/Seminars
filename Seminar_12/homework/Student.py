# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.
import csv


class Names:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.check_name(value)
        setattr(instance, self.param_name, value)

    def check_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Имя и Фамилия должны быть строками')
        if not value.isalpha() or not value.istitle():
            raise ValueError('Имя и Фамилия должны быть из букв и начинаться с заглавной')


class Range:
    MIN_GRADE = 2
    MAX_GRADE = 5
    MIN_TEST_SCORE = 0
    MAX_TEST_SCORE = 100

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def check_grades(self):
        if not isinstance(self.value, int):
            raise TypeError('Оценка должна быть целым числом')
        if not self.MIN_TEST_SCORE <= self.value <= self.MAX_GRADE:
            raise ValueError(f'Значение {self.value} должно быть больше или равно {self.MIN_TEST_SCORE} '
                             f'и меньше или равно {self.MAX_GRADE}')

    def check_test_scores(self):
        if not isinstance(self.value, int):
            raise TypeError('Оценка должна быть целым числом')
        if not self.MIN_GRADE <= self.value <= self.MAX_TEST_SCORE:
            raise ValueError(f'Значение {self.value} должно быть больше или равно {self.MIN_GRADE} '
                             f'и меньше или равно {self.MAX_TEST_SCORE}')


class Student:
    firstname = Names()
    lastname = Names()

    def __init__(self, firstname, lastname):
        self.subject = None
        self.firstname = firstname
        self.lastname = lastname

        with open('subjects.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            self.subjects = [i for i in next(reader)[0].split(';')]
        for subject in self.subjects:
            setattr(Student, subject, dict(grades=[], tests_scores=[]))

    def set_grade(self, subject, grades_or_tests, grade):
        types_of_grades = ['оценка', 'тест']
        if subject not in self.subjects:
            raise NameError(f'Студент не изучает {subject}')
        if grades_or_tests not in types_of_grades:
            raise NameError(f'Студент не получает оценки типа {grades_or_tests}')
        match grades_or_tests:
            case 'оценка':
                Range(grade).check_grades()
                self.__getattribute__(subject)['grades'].append(grade)
            case 'тест':
                Range(grade).check_test_scores()
                self.__getattribute__(subject)['tests_scores'].append(grade)

    def average_score(self):
        average_test_score_in_subjects = {}
        for subject in self.subjects:
            test_score = self.__getattribute__(subject)['tests_scores']
            if test_score is not None and len(test_score) != 0:
                average_test_score_in_subjects.setdefault(f'{subject}', sum(test_score) / len(test_score))

        all_grades = []
        for subject in self.subjects:
            grades = sum(self.__getattribute__(subject)['grades'])
            if grades is not None:
                all_grades.append(grades)
            average_all_grades = sum(all_grades) / len(all_grades) if len(all_grades) != 0 else 0

        print('Средние баллы по тестам для каждого предмета:')
        for key, value in average_test_score_in_subjects.items():
            print("{0}: {1}".format(key, value))
        print('\nСредний балл по оценкам всех предметов вместе взятых:')
        print(round(average_all_grades, 2), end='\n')

    def __str__(self):
        lessons = '\n'.join(f'{self.subject} = {self.__getattribute__(self.subject)}'
                            for self.subject in self.subjects)
        return f'{self.firstname} {self.lastname}\n' \
               f'Оценки:\n{lessons}'


def create_csv():
    with open('subjects.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(('литература', 'география', 'алгебра', 'геометрия'))


if __name__ == '__main__':
    # create_csv()
    student1 = Student('Mark', 'Green')
    student1.set_grade('литература', 'оценка', 3)
    student1.set_grade('литература', 'тест', 80)
    student1.set_grade('алгебра', 'оценка', 5)
    student1.set_grade('география', 'тест', 65)
    student1.set_grade('геометрия', 'оценка', 5)
    student1.set_grade('геометрия', 'тест', 87)
    print(student1)
    student1.average_score()
    # student2 = Student('Mason', 'Black')
    # student2.set_grade('алгебра', 'оценка', 4)
    # student2.set_grade('литература', 'тест', 87)
    # student2.set_grade('геометрия', 'оценка', 4)
    # student2.set_grade('география', 'тест', 98)
    # print(student2)
    # student3 = Student('Jason', 'White')
    # student3.set_grade('алгебра', 'оценка', 5)
    # student3.set_grade('алгебра', 'тест', 101)
    # student3.set_grade('геометрия', 'оценка', 4)
    # student3.set_grade('геометрия', 'тест', 89)
    # print(student3)
