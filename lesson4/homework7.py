from itertools import count
from math import factorial


def my_func():
    for i in count(1):
        yield factorial(i)


num = int(input('Введите число, до которого показать факториал: '))
fact = my_func()
if num > 0:
    a = 1
    for i in fact:
        if a <= num:
            print(f'факториал {a} = {i}')
            a += 1
else:
    num = 0
    print(0)

