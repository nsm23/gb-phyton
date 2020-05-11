from sys import argv

script_name, pay_rate, t_time, bonus = argv
try:
    pay_rate = int(pay_rate)
    t_time = int(t_time)
    bonus = int(bonus)
    salary = pay_rate * t_time + bonus
    print(f"Вы заработали -  {salary}$")

except ValueError:
    print('Enter number')
