from itertools import count, cycle


def count_func(num, end_num):
    try:
        num = int(num)
        end_num = int(end_num)
        for el in count(num):
            if el > end_num:
                break
            else:
                print(el)
    except ValueError:
        print('ValueError - Enter "int" number')


count_func(num=input('enter "number" - '), end_num=input('enter "end number" - '))

def cycle_func(n):
    my_list = [1, 2, True, 'Hello', 23.3, None]
    print(my_list)
    count = 1
    for i in cycle(my_list):
        if count > n:
            break
        else:
            print(f'{i} -- {type(i)}')
            count += 1


cycle_func(n = int(input('Enter iteration: ')))
