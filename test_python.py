from quiz import birthday

# Функция filter
def test_filter_by_year():
    def filter_by_year(item):
        key, value = item
        year = int(value.split('.')[2])
        return year < 1820

    filtered_items = filter(filter_by_year, birthday.items())
    filtered_dict = dict(filtered_items)

    expected_result = {
        'Н.В. Гоголь': '20.03.1809',
        'А.С. Пушкин': '06.06.1799',
        'М.Ю. Лермонтов': '15.10.1814',
        'И.С. Тургенев': '09.11.1818',
        'И.А. Гончаров': '18.06.1812'}

    assert filtered_dict == expected_result

# Функция map
def test_format_date():
    def format_date(item):
        key, value = item
        day, month, year = value.split('.')
        return key, f'{day}/{month}/{year}'

    # Применение функции map()
    formatted_items = map(format_date, birthday.items())

    # Преобразование результата в словарь
    formatted_dict = dict(formatted_items)

    expected_result = {
        'А.И. Куприн': '07/09/1870',
        'Н.В. Гоголь': '20/03/1809',
        'А.П. Чехов': '29/01/1860',
        'А.С. Пушкин': '06/06/1799',
        'М.Ю. Лермонтов': '15/10/1814',
        'Н.А. Некрасов': '10/12/1821',
        'И.С. Тургенев': '09/11/1818',
        'Л.Н. Толстой': '09/09/1828',
        'И.А. Гончаров': '18/06/1812',
        'А.Н. Толстой': '10/01/1883'}

    assert formatted_dict == expected_result

def test_sorted_birthdays():
    def get_birth_date(item):
        return item[1]

    # Сортируем словарь по значениям (датам рождения)
    sorted_birthdays = dict(sorted(birthday.items(), key=get_birth_date))

    # Проверяем результаты
    expected_result = {
        'А.С. Пушкин': '06.06.1799',
        'Н.В. Гоголь': '20.03.1809',
        'И.А. Гончаров': '18.06.1812',
        'М.Ю. Лермонтов': '15.10.1814',
        'И.С. Тургенев': '09.11.1818',
        'Н.А. Некрасов': '10.12.1821',
        'Л.Н. Толстой': '09.09.1828',
        'А.П. Чехов': '29.01.1860',
        'А.И. Куприн': '07.09.1870',
        'А.Н. Толстой': '10.01.1883'}

    assert sorted_birthdays == expected_result
