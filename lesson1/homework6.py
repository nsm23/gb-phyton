a = float(input('Какое расстояние Вы пробежали в первый день? '))
b = float(input('Какого результата хотите достичь? '))
per_cent = 0.1  # ежедневный процент увеличения
day = 1

while a < b:
    a = a + a * per_cent
    day += 1
print(f'Нужного результата вы достигните на %.d' % day, 'день')

