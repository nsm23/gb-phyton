season_list = ['Весна', 'Лето', 'Осень', 'Зима']
season_dict = {1: 'Весна', 2: 'Лето', 3: 'Осень', 4: 'Зима'}
mounth = int(input('Введите номер месяца "от 1 до 12": '))
if 1 <= mounth <= 12:
    if mounth == 3 or mounth == 4 or mounth == 5:
        print('Время года - ', season_list[0], '(список)')  # Можно было в один print оформить.
        print('Время года - ', season_dict.get(1), '(словарь)')
    elif mounth == 6 or mounth == 7 or mounth == 8:
        print('Время года - ', season_list[1], '(список)')
        print('Время года - ', season_dict.get(2), '(словарь)')
    elif mounth == 9 or mounth == 10 or mounth == 11:
        print('Время года - ', season_list[2], '(список)')
        print('Время года - ', season_dict.get(3), '(словарь)')
    else:
        print('Время года - ', season_list[3], '(список)')
        print('Время года - ', season_dict.get(1), '(словарь)')
else:
    print('Нет такого месяца')
