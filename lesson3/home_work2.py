"""
enter data

name = input('Enter name: ')
surname = input('Enter surname: ')
age = int(input('Enter age: '))
city = input('Enter your city of residence')
tel = int(input('Enter mobile number: '))
mail = input('Enter your e-mail: ')
"""
def main(name, surname, age, city, tel, mail):
    return ' '.join([name, surname, age, city, tel, mail])


print(main(name='Sergey', surname='Nabiullin', age='36',
           city='Moscow', tel='+7926****', mail='example@mail.ru'))
