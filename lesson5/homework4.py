trans_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_list = []
with open('text_4.txt', 'r') as my_file:
    for i in my_file:
        i = i.split(' ', 1)
        my_list.append(trans_dict[i[0]] + i[1])
print(my_list)
with open('new_text4.txt', 'w') as my_f:
    my_f.writelines(my_list)
print(my_list, file=open("new_text4.txt", 'w'))
