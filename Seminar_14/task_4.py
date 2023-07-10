# Задание №4
# Напишите для задачи 1 тесты pytest. Проверьте следующие
# варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import pytest
from task_1_2 import remove_chars


def test_no_changes():
    assert remove_chars('dfdfhdfh wreg') == 'dfdfhdfh wreg'


def test_register_conversion():
    assert remove_chars('dFDfhdfh WREG') == 'dfdfhdfh wreg'


def test_remove_punctuation():
    assert remove_chars('bg!&&,.j j:;') == 'bgj j'


def test_removing_cyrillic():
    assert remove_chars('валджьЬОП') == ''


def test_all_changes():
    assert remove_chars('dfkLLLLmbn ;!ICL роивмghv;!!!') == 'dfkllllmbn icl ghv'


if __name__ == '__main__':
    pytest.main(['-v'])
