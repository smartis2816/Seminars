# Задание №3
# Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)
import unittest
from task_1_2 import remove_chars


class TestChars(unittest.TestCase):
    def test_no_changes(self):
        self.assertEqual(remove_chars('dfdfhdfh wreg'), 'dfdfhdfh wreg')

    def test_register_conversion(self):
        self.assertEqual(remove_chars('dFDfhdfh WREG'), 'dfdfhdfh wreg')

    def test_remove_punctuation(self):
        self.assertEqual(remove_chars('bg!&&,.j j:;'), 'bgj j')

    def test_removing_cyrillic(self):
        self.assertEqual(remove_chars('валджьЬОП'), '')

    def test_all_changes(self):
        self.assertEqual(remove_chars('dfkLLLLmbn ;!ICL роивмghv;!!!'), 'dfkllllmbn icl ghv')


if __name__ == '__main__':
    # print(remove_chars('dfsBKdjnb апвыривтп2462'))
    unittest.main(verbosity=True)
