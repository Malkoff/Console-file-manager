import os
import shutil


def operations():
    print('*' * 20)
    print('1. Директорию')
    print('2. Папки')
    print('3. Файлы')
    print('4. Создать папку')
    print('5. Удаление (папки/файла)')
    print('6. Копирование (папки/файла)')
    print('7. Назад')
    print('*' * 20)
    choice = input('Выберите пункт: ')
    if choice == '1':
        print(os.listdir())
        return operations()
    elif choice == '2':
        for folder in os.listdir():
            if os.path.isdir(folder):
                print('Папка: ', folder)
        return operations()
    elif choice == '3':
        for file in os.listdir():
            if os.path.isfile(file):
                print('Файл: ', file)
        return operations()
    elif choice == '4':
        new_folder = input('Введите имя папки для создания: ')
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
            print('Папка успешно создана')
        else:
            print('Папка с таким именем уже существует')
        return operations()
    elif choice == '5':
        del_folder = input('Введите имя папки для удаления: ')
        if os.path.exists(del_folder):
            shutil.rmtree(del_folder)
            print('Папка успешно удалена')
        else:
            print('Папка с таким именем не существует')
        return operations()
    elif choice == '6':
        sel_folder = input('Выберете папку для копирования: ')
        copy_folder = input('Введите новое имя папки: ')
        if os.path.exists(sel_folder) and not os.path.exists(copy_folder):
            shutil.copytree(sel_folder, copy_folder)
            print('Папка успешно скопирована')
        else:
            print('Исходная папка не существует или целевая папка уже существует')
        return operations()
    elif choice == '7':
        return