try:
    with open('text_5.txt', 'w') as my_file:
        numbers = input('Enter a numbers by space: ')
        my_file.writelines(numbers)
        total = sum(map(int, numbers.split()))
        print(f'\nСумма введенных чисел = {total}', file=my_file)  # Или просто print(total) в консоль
except ValueError:
    print('Error - Enter  numbers')
except IOError:
    print('Error int/out')
