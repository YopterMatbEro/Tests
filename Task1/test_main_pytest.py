from secretary import secretary_program_start


def test_all_people(monkeypatch):
    inputs = iter(['ap', 'q'])
    expected = {'Аристарх Павлов', 'Геннадий Покемонов', 'Василий Гупкин'}

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert secretary_program_start() == expected


def test_people(monkeypatch):
    inputs = iter(['p', '2207 876234', 'q'])
    expected = 'Василий Гупкин'
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert secretary_program_start() == expected


def test_list(monkeypatch):
    inputs = iter(['l', 'q'])
    expected = ['passport "2207 876234" "Василий Гупкин"',
                'invoice "11-2" "Геннадий Покемонов"',
                'insurance "10006" "Аристарх Павлов"']
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert secretary_program_start() == expected


def test_shelf(monkeypatch):
    inputs = iter(['s', '11-2', 'q'])
    expected = '1'
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert secretary_program_start() == expected


def test_add(monkeypatch):
    inputs = iter(['a', '1613', 'reference from doctor', 'ЖОзефина ПАвловна', '3', 's', '1613', 'q'])
    # expected = '\nНа полку "3" добавлен новый документ'  # результат, если убрать inputs 's', '1613'
    expected = '3'
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert secretary_program_start() == expected


def test_delete(monkeypatch):
    inputs = iter(['d', '11-2', 'q'])
    expected = 'Документ с номером "11-2" был успешно удален'
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert secretary_program_start() == expected
    inputs = iter(['d', '111', 'q'])
    expected = 'Документ с указанным номером не существует'
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert secretary_program_start() == expected


def test_move(monkeypatch):
    inputs = iter(['m', '11-2', '3', 'q'])
    expected = 'Документ номер "11-2" был перемещен на полку номер "3"'
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert secretary_program_start() == expected


def test_add_shelf(monkeypatch):
    inputs = iter(['as', '5', 'q'])
    expected = 'Добавлена полка "5"'
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert secretary_program_start() == expected
