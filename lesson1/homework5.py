revenue = float(input('Какая выручка у Вашей фирмы? $'))
costs = float(input('Какие затраты у Вашей фирмы? $'))
profit = revenue - costs
if profit > 0:
    margin = profit / revenue  # В проценты не переводил
    print('Ура! Вы смогли заработать!\nВаша рентабельность: %.2f' % margin)
    print()
    staff = int(input('Сколько сотрудников работает у Вас? '))
    prof_staff = profit / staff
    print('Прибыль фирмы в расчёте на 1 сотрудника - %.2f' % prof_staff, '$')
elif profit == 0: # revenue == coast
    print('Вам нужно лучше работать!')

else:
    print('Вам пора закрываться!')
