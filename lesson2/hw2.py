my_list = []
el = int(input('Сколько элементов хотите добавить в список? '))
for i in range(0, el):
    n = int(input('Введите целое число: '))
    my_list.append(n)
print(my_list, '- Исходный список')
for i in range(0, len(my_list) - 1):
    if i % 2 == 0:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        i += 2
print(my_list, '- Измененный список')
