from random import randint

my_list = [randint(0, 347) for el in range(8)]
new_list = [el for num, el in enumerate(my_list) if my_list[num] > my_list[num - 1]]
print(f'{my_list} \n{new_list}')

