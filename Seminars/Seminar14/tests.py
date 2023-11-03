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
from task2 import remove_char

class TestRemove_char(unittest.TestCase):
    def test_no_change(self):
        self.assertEquals(remove_char("qwer"), "qwer")

    def test_result_is_str(self):
        self.assertIsInstance(remove_char("qwer"), str)

    def test_in(self):
        self.assertIn(" ", remove_char("qw er"))

    def test_notnone(self):
        self.assertIsNone(remove_char("qwer"))


if __name__ == '__main__':
    unittest.main(verbosity=2)

