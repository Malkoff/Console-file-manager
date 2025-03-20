import os
from traceback import format_exc

history = []

FILE_NAME_1 = 'bank.txt'
FILE_NAME_2 = 'orders.txt'


if not os.path.exists(FILE_NAME_1):
    balance = 0
else:
    with open(FILE_NAME_1, 'r') as f:
        balance = int(f.readline())

if os.path.exists(FILE_NAME_2):
    with open(FILE_NAME_2, 'r') as f:
        for order in f:
            history.append(order.replace('\n', ''))


def check():
    global balance, history
    print('*' * 20)
    print(f'ВАШ БАЛАНС: {balance}')
    print('1. Пополнение счета')
    print('2. Покупка')
    print('3. История покупок')
    print('4. Назад')
    print('*' * 20)
    choice = input('Выберите пункт меню: ')
    if choice == '1':
        balance += int(input('Введите сумму для пополнения: '))
        print(f'Сумма {balance} поступила на счет')
        return check()
    elif choice == '2':
        name = input('Введите наименование покупки: ')
        cost = int(input('Введите цену покупки: '))
        order = (name, cost)
        history.append(order)
        if cost > balance:
            print('Недостаточно средств на балансе')
        elif cost <= balance:
            balance -= cost
        return check()
    elif choice == '3':
        buy = list(history)
        print(f'Ваша история покупок\n {buy}')
        return check()
    elif choice == '4':
        with open(FILE_NAME_1, 'w') as f:
            f.write(str(balance))
        with open(FILE_NAME_2, 'w', encoding='utf-8') as f:
            f.write(str(history))
        return
    else:
        print('Ошибка, неверный пункт!')
        return check()

# check()