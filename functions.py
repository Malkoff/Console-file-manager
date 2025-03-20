# Чистая функция на счет
def check(balance, history, choice, amount=None, purchase=None, name=None):
    if choice == '1':
        new_balance = balance + amount
        return new_balance, history
    elif choice == '2':
        if purchase > balance:
            return balance, history
        else:
            new_balance = balance - purchase
            new_history = history + [[name, purchase]]
            return new_balance, new_history
    elif choice == '3':
        return balance, history  # История покупок не изменяется, поэтому просто возвращаем текущие значения
    elif choice == '4':
        return balance, history
    else:
        return balance, history  # В случае неверного выбора, возвращаем текущие значения

# Пример использования функции
balance = 0
history = []

# Пример пополнения счёта
balance, history = check(balance, history, '1', amount=100)
print(f'Конечный баланс: {balance}')
print(f'История покупок: {history}')

# Пример покупки
balance, history = check(balance, history, '2', purchase=50, name='Товар 1')
print(f'Конечный баланс: {balance}')
print(f'История покупок: {history}')




# Чистая функция на файловый менеджер
import os
import shutil

def operations(choice, folder_name=None, new_folder_name=None):
    if choice == '1':
        return os.listdir()
    elif choice == '2':
        return [folder for folder in os.listdir() if os.path.isdir(folder)]
    elif choice == '3':
        return [file for file in os.listdir() if os.path.isfile(file)]
    elif choice == '4':
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            return f"Папка {folder_name} успешно создана"
        else:
            return f"Папка с именем {folder_name} уже существует"
    elif choice == '5':
        if os.path.exists(folder_name):
            if os.path.isfile(folder_name):
                os.remove(folder_name)
                return f"Файл {folder_name} успешно удален"
            else:
                shutil.rmtree(folder_name)
                return f"Папка {folder_name} успешно удалена"
        else:
            return f"Элемент с именем {folder_name} не существует"
    elif choice == '6':
        if os.path.exists(folder_name) and not os.path.exists(new_folder_name):
            shutil.copytree(folder_name, new_folder_name)
            return f"Папка {folder_name} успешно скопирована в {new_folder_name}"
        else:
            return f"Исходная папка {folder_name} не существует или целевая папка {new_folder_name} уже существует"
    elif choice == '7':
        return "Назад"
    else:
        return "Некорректный выбор"





def victory(writers, birthday, answers):
    list_errors = []
    for surname, answer in zip(writers, answers):
        correct_answer = birthday[surname]
        if answer != correct_answer:
            list_errors.append(1)
        else:
            list_errors.append(0)
    error = sum(list_errors)
    correct = len(list_errors) - error
    return correct, error, correct * 100 / len(list_errors)

#Пример использования функции
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

# Пример списка писателей и ответов
writers = ['А.И. Куприн', 'Н.В. Гоголь', 'А.П. Чехов', 'А.С. Пушкин', 'М.Ю. Лермонтов']
answers = ['07.09.1870', '20.03.1809', '29.01.1860', '06.06.1799', '15.10.1814']

correct, error, percentage = victory(writers, birthday, answers)
print(f'Количество правильных ответов: {correct}')
print(f'Количество ошибок: {error}')
print(f'Процент правильных ответов: {percentage}%')

