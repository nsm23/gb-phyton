with open('text.txt', 'w') as my_file:
    while True:
        word = input('Enter data: ')
        if word == '':
            break
        else:
            my_file.writelines(word + '\n')

with open('text.txt', 'r') as my_file:
    st = 0  # строчечка
    bk = 0  # буквочка
    line = my_file.readlines()
    for i in range(len(line)):
        st += 1
        bk += len(line[i]) - 1
        print(f'Line {i + 1} \t\tnumber of characters {len(line[i]) -1}')
    print('**********************************')
    print(line)
    print('**********************************')
    print(f'Total lines in the file: {st}\nTotal characters without enter: {bk}')

with open('text.txt', 'r') as my_file:
    wrd = my_file.read()
    wrd = wrd.split()
    print(f'Total words - {len(wrd)}')
