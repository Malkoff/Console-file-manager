import sys
from quiz import victory
from bank_account import check
from menu import main_menu
from file_operations import operations

balance = 0
history = []

while True:
    main_menu()
    choice = input('Выберите пункт: ')
    if choice == '1':
        operations()
    elif choice == '2':
        print(f'Ваша операционная система: {sys.platform}')
        print(f'Данные о программе: {sys.version}')
    elif choice == '3':
        print('Создал - Малков Григорий Михайлович')
    elif choice == '4':
        victory()
    elif choice == '5':
        check()
    elif choice == '6':
        break
    else:
        print('Неверный пункт!')