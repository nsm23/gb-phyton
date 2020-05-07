a = int(input('Введите количество секунд: '))
seconds = a % 60
minutes = a // 60 % 60
hours = a // 3600
print("%02d:%02d:%02d" % (hours, minutes, seconds))
