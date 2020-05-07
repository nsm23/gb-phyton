def my_sum(*args):
    total = 0
    a = False
    while a == False:
        num = input('enter a numbers by spaces, or "q" for quit: ').split()
        amount = 0
        for i in range(len(num)):
            if num[i] == 'q' or num[i] == 'Q':
                a = True
                break
            else:
                amount += int(num[i])
        total += amount
        print(f'summa - {amount}')
        print(f'total - {total}')

my_sum()