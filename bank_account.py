balance = 0
history = []


def check():
    global balance, history
    print('*' * 20)
    print(f'ВАШ БАЛАНС: {balance}')
    print('1. Пополнение счета')
    print('2. Покупки')
    print('3. История покупок')
    print('4. Назад')
    print('*' * 20)
    choice = input('Выберите пункт меню: ')
    if choice == '1':
        balance += int(input('Введите сумму для пополнения: '))
        print(f'Сумма {balance} поступила на счет')
        return check()
    elif choice == '2':
        purchase = int(input('Введите сумму покупки: '))
        if purchase > balance:
            print('Недостаточно средств на балансе')
        elif purchase <= balance:
            name = input('Введите наименование покупки: ')
            balance -= purchase
            history.append([name, purchase])
        return check()
    elif choice == '3':
        buy = list(history)
        print(f'Ваша история покупок\n {buy}')
        return check()
    elif choice == '4':
        return
    else:
        print('Ошибка, неверный пункт!')
        return check()