from functools import reduce


def my_func(pr_el, el):
    return pr_el * el


print(f'List of event numbers - {[el for el in range(100, 1001, 2)]}')
print('Product of data:', (reduce(my_func, [el for el in range(100, 1001, 2)])))

# _________________________________________________________________________________________

my_list = [el for el in range(100, 1001, 2)]


def my_funct(a, b):
    return a * b


print('Второй вариант: ', reduce(my_funct, my_list))
