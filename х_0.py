#Вывод игрового поля
def print_field(id):
    for axis in range(len(id[0])):
        print('{:^4}'.format(id[0][axis]), end='')
    print()
    for row in range(1, len(id)):
        for col in range(len(id[row])):
            print('{:^3}|'.format(id[row][col]), end='')
        print('\n')
#Ввод имен участников
def initial_game():
    name = {'X': '', '0': ''}
    name['X'] = input(f'Введите имя игрока играющего "{list(name.keys())[0]}"-м: ')
    name['0'] = input(f'Введите имя игрока играющего "{list(name.keys())[1]}"-м: ')
    return name
#Ввод значений
def input_value_x(id, point):
    print(f'Ходит игрок {list(point.values())[0]}')
    print(f'Для установки "{list(point.keys())[0]}" введите цифровое обозначение строки, затем цифровое обозначение столбца')
    row = int(input('Введите значение строки от 0 до 2 и нажмите "Enter": '))
    col = int(input('Введите значение столбца от 0 до 2 и нажмите "Enter": '))
    if (row not in range(0, 3)) or (col not in range(0, 3)):
        print('Вы ввели неверное значение строки/колонки')
        input_value_x(id, point)
    elif id[row+1][col+1] != '':
        print('Вы ввели значение в занятое поле')
        input_value_x(id, point)
    else:
        id[row + 1][col + 1] = 'X'
        print('Вы сделали ход:')
        print_field(id)
#Ввод значения поля
def input_value_0(id, point):
    print(f'Ходит игрок {list(point.values())[1]}')
    print(f'Для установки "{list(point.keys())[1]}" введите цифровое обозначение строки, затем цифровое обозначение столбца')
    row = int(input('Введите значение строки от 0 до 2 и нажмите "Enter": '))
    col = int(input('Введите значение столбца от 0 до 2 и нажмите "Enter": '))
    if (row not in range(0, 3)) or (col not in range(0, 3)):
        print('Вы ввели неверное значение строки/колонки')
        input_value_0(id, point)
    elif id[row+1][col+1] != '':
        print('Вы ввели значение в занятое поле')
        input_value_0(id, point)
    else:
        id[row + 1][col + 1] = '0'
        print('Вы сделали ход:')
        print_field(id)
#Проверка строк
def checking_rows(id, point):
    for row in id[1:]:
        if row[1:].count(point) == 3:
            return True
    return False
#Проверка колонок
def checking_col(id, point):
    for row in range(1, len(id)):
        count = 0
        for col in range(1, len(id[row])):
            if id[col][row] == point:
                count += 1
        if count == 3:
            return True
    return False
#Проверка диагоналей
def checking_diag(id, point):
    count = 0
    count_reverse = 0
    for row in range(1, len(id)):
        if id[row][row] == point:
            count += 1
        if id[row][4-row] == point:
            count_reverse += 1
    if count == 3 or count_reverse == 3:
        return True
    else:
        return False
#Проверка всех условий
def checking_field(id, point):
    if checking_rows(id, point):
        return True
    elif checking_col(id, point):
        return True
    elif checking_diag(id, point):
        return True
    else:
        return False
#Проверка свободных полей
def end_of_point(id):
    count = 0
    for row in range(1, len(id)):
        for col in range(1, len(id[row])):
            if id[row][col]!='':
                count += 1
    if count == 9:
        return True
    else:
        return False
#Игра
def game(id, names):
    input_value_x(id, names)
    if checking_field(id, 'X'):
        print('Победил игрок: {}'.format(names['X']))
    elif end_of_point(id) == True:
        print('Ничья! Победила дружба.')
    else:
        input_value_0(id, names)
        if checking_field(id, '0'):
            print('Победил игрок: {}'.format(names['0']))
        elif end_of_point(id) == True:
            print('Ничья! Победила дружба.')
        else:
            game(id, names)
#Запуск игры
def load():
    id = [
        ['', '0', '1', '2'],
        ['0', '', '', ''],
        ['1', '', '', ''],
        ['2', '', '', '']
    ]
    print_field(id)
    names = initial_game()
    game(id, names)
    print('Желаете сыграть еще раз?')
    y_n = input('Введите "Y", если хотите сыграть еще раз, "N", если нет: ')
    if y_n.lower() == 'y':
        load()
    else:
        print('До новых встреч!')

load()


