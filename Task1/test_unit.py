from secretary import secretary_program_start
from unittest.mock import patch
import unittest


class MyTestCase(unittest.TestCase):
    def test_all_people(self):
        self.inputs = iter(['ap', 'q'])
        self.expected = {'Аристарх Павлов', 'Геннадий Покемонов', 'Василий Гупкин',
                         'Джеймс Бонд', 'ЖОзефина ПАвловна'}
        with patch('builtins.input', side_effect=lambda _: next(self.inputs)):
            assert secretary_program_start() == self.expected

    def test_people(self):
        self.inputs = iter(['p', '2207 876234', 'p', '11-2', 'q'])
        with patch('builtins.input', side_effect=lambda _: next(self.inputs)):
            assert secretary_program_start() == 'Василий Гупкин'
            assert secretary_program_start() == 'Геннадий Покемонов'

    def test_list(self):
        self.inputs = iter(['l', 'q'])
        self.expected = ['passport "2207 876234" "Василий Гупкин"',
                         'invoice "11-2" "Геннадий Покемонов"',
                         'insurance "10006" "Аристарх Павлов"']
        with patch('builtins.input', side_effect=lambda _: next(self.inputs)):
            assert secretary_program_start() == self.expected

    def test_shelf(self):
        self.inputs = iter(['s', '11-2', 's', '10006', 'q'])
        with patch('builtins.input', side_effect=lambda _: next(self.inputs)):
            assert secretary_program_start() == '1'
            assert secretary_program_start() == '2'

    def test_add(self):
        self.inputs = iter(['a', '1613', 'reference from doctor', 'ЖОзефина ПАвловна', '3', 's', '1613', 'q'])
        with patch('builtins.input', side_effect=lambda _: next(self.inputs)):
            assert secretary_program_start() == '3'
            self.inputs = iter(['a', '777', 'certificate', 'Джеймс Бонд', '2', 's', '777', 'q'])
            assert secretary_program_start() == '2'

    def test_delete(self):
        self.inputs = iter(['d', '1613', 'd', '777', 'q'])
        with patch('builtins.input', side_effect=lambda _: next(self.inputs)):
            assert secretary_program_start() == 'Документ с номером "1613" был успешно удален'
            assert secretary_program_start() == 'Документ с номером "777" был успешно удален'

    def test_move(self):
        self.inputs = iter(['m', '11-2', '3', 'm', '11-2', '1', 'q'])
        with patch('builtins.input', side_effect=lambda _: next(self.inputs)):
            assert secretary_program_start() == 'Документ номер "11-2" был перемещен на полку номер "3"'
            assert secretary_program_start() == 'Документ номер "11-2" был перемещен на полку номер "1"'

    def test_add_shelf(self):
        self.inputs = iter(['as', '5', 'as', 'kek', 'q'])
        with patch('builtins.input', side_effect=lambda _: next(self.inputs)):
            assert secretary_program_start() == 'Добавлена полка "5"'
            assert secretary_program_start() == 'Добавлена полка "kek"'


if __name__ == '__main__':
    unittest.main()
