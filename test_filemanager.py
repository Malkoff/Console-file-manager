import os, shutil
from functions import check, operations, victory

def test_check_function():
    # Исходные данные
    initial_balance = 0
    initial_history = []

    # Тестирование пополнения счёта
    balance, history = check(initial_balance, initial_history, '1', amount=100)
    assert balance == 100
    assert history == []

    # Тестирование покупки
    balance, history = check(balance, history, '2', purchase=50, name='Товар 1')
    assert balance == 50
    assert history == [['Товар 1', 50]]

    # Тестирование неверного выбора
    balance, history = check(balance, history, '5')
    assert balance == 50
    assert history == [['Товар 1', 50]]

    # Тестирование истории покупок
    balance, history = check(balance, history, '3')
    assert balance == 50
    assert history == [['Товар 1', 50]]

    # Тестирование выхода
    balance, history = check(balance, history, '4')
    assert balance == 50
    assert history == [['Товар 1', 50]]





def test_operations_function():
    # Тестирование вывода списка директорий
    result = operations('1')
    assert isinstance(result, list)

    # Тестирование вывода списка папок
    result = operations('2')
    assert isinstance(result, list)
    for item in result:
        assert os.path.isdir(item)

    # Тестирование вывода списка файлов
    result = operations('3')
    assert isinstance(result, list)
    for item in result:
        assert os.path.isfile(item)

    # Тестирование создания папки
    folder_name = 'new_folder'
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)
    result = operations('4', folder_name)
    assert result == f"Папка {folder_name} успешно создана"
    assert os.path.exists(folder_name)

    # # Тестирование копирования папки
    # source_folder = 'source_folder'
    # target_folder = 'target_folder'
    # os.makedirs(source_folder, exist_ok=True)
    # result = operations('6', source_folder, target_folder)
    # assert result == f"Папка {source_folder} успешно скопирована в {target_folder}"
    # assert os.path.exists(target_folder)

    # Тестирование удаления папки
    result = operations('5', folder_name)
    assert result == f"Папка {folder_name} успешно удалена"
    assert not os.path.exists(folder_name)

    # Тестирование возврата при выборе '7'
    result = operations('7')
    assert result == "Назад"

    # Тестирование некорректного выбора
    result = operations('8')
    assert result == "Некорректный выбор"






def test_victory():
    birthday = {
        'А.И. Куприн': '07.09.1870',
        'Н.В. Гоголь': '20.03.1809',
        'А.П. Чехов': '29.01.1860',
        'А.С. Пушкин': '06.06.1799',
        'М.Ю. Лермонтов': '15.10.1814',
        'Н.А. Некрасов': '10.12.1821',
        'И.С. Тургенев': '09.11.1818',
        'Л.Н. Толстой': '09.09.1828',
        'И.А. Гончаров': '18.06.1812',
        'А.Н. Толстой': '10.01.1883'
    }

    writers = ['А.И. Куприн', 'Н.В. Гоголь', 'А.П. Чехов', 'А.С. Пушкин', 'М.Ю. Лермонтов']
    answers = ['07.09.1870', '20.03.1809', '29.01.1860', '06.06.1799', '15.10.1814']

    correct, error, percentage = victory(writers, birthday, answers)
    assert correct == 5
    assert error == 0
    assert percentage == 100.0

def test_victory_with_errors():
    birthday = {
        'А.И. Куприн': '07.09.1870',
        'Н.В. Гоголь': '20.03.1809',
        'А.П. Чехов': '29.01.1860',
        'А.С. Пушкин': '06.06.1799',
        'М.Ю. Лермонтов': '15.10.1814',
        'Н.А. Некрасов': '10.12.1821',
        'И.С. Тургенев': '09.11.1818',
        'Л.Н. Толстой': '09.09.1828',
        'И.А. Гончаров': '18.06.1812',
        'А.Н. Толстой': '10.01.1883'
    }

    writers = ['А.И. Куприн', 'Н.В. Гоголь', 'А.П. Чехов', 'А.С. Пушкин', 'М.Ю. Лермонтов']
    answers = ['07.09.1870', '21.03.1809', '28.01.1860', '06.06.1799', '16.10.1814']  # Ошибки в ответах

    correct, error, percentage = victory(writers, birthday, answers)
    assert correct == 2
    assert error == 3
    assert percentage == 40.0
