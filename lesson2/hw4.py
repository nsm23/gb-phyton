my_list = []
a = int(input('Сколько слов хотите использовать? '))
for i in range(0, a):
    b = input('Введите слово: ')
    my_list.append(b)
print(f'Строка: ', ' '.join(my_list))
if len(str(my_list)) >= 10:
    for i in range(0, len(my_list)):
        print(f'{i+1}. {my_list[i] [0:10]}')
else:
    for i in range(0, len(my_list)):
        print(f'{i+1}. {my_list[i]}')


