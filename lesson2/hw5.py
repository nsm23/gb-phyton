my_list = [7, 5, 3, 3, 2]
print(f'Рейтинг:  {my_list}')
num = int(input('Введите число, или "555", для завершения: '))
while num != 555:
    n = my_list.count(num)
    for i in my_list:
        if n > 0:
            digit = my_list.index(num)
            my_list.insert((digit + n), num)
            break
        else:
            if num > i:
                dig = my_list.index(i)
                my_list.insert(dig, num)
                break
            elif num < my_list[len(my_list) - 1]:
                my_list.append(num)
    print('Обновленный рейтинг - ', my_list)
    num = int(input('Хотите ввести еще одно значение? '))

