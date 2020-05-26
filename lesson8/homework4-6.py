"""
def display menu()
LOOK = 1
ADD = 2
CHANGE = 3
EXIT = 4
Идея такая...
print('Menu')
print('Показать текущие остатки на складе = 1')
print('Добавить товар = 2')
print('Посмотреть остаток по принтерам/сканерам... = 3)
print('Выход = 4')
choice = 0
while choice != exit
choice = int(input('Введите вариант: )
остальное сделать модулем и импортировать
"""

class Office_eqip:

    def __init__(self, name, price, quantity, tecnics, id, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.id = id
        self.store = []
        self.my_dict = {}
        self.tecnics = tecnics


    def income(self):
        with open('homework4-6.txt', 'a', encoding='utf-8') as my_f:
            try:
                id = 0
                while input('Add product, enter"y/n": ') == 'y':
                    name = input('Введите наименование: ')
                    prise = float(input('Введите стоимость: '))
                    quantity = int(input('Введите количество: '))
                    tecnics = input('Введите вид техники: ')
                    id +=1
                    my_f.writelines(name + ' ' + str(prise) + ' ' + str(quantity) + ' ' + tecnics + ' ' + str(id) +'\n')
                    self.my_dict[name] = [prise, quantity, tecnics, id]
                self.store.append(self.my_dict)
                print(f'Список: {self.store}')
                
            except:
                return 'in\out Error'

class Printer(Office_eqip):
    @property
    def my_print(self):
        self.dic = {}
        with open('homework4-6.txt', 'r', encoding='utf-8') as my_f:
            my_f.seek(0)
            for i in my_f:
                name, price, quantity, tecnics, id = i.split()
                if tecnics == 'printer':
                    self.dic[tecnics] = [name, quantity]
            return self.dic





class Scanner(Office_eqip):
    def my_scan(self):
        pass
class Copier(Office_eqip):
    def my_copier(self):
        pass


#b = Office_eqip('Hp', 1500, 12, 'printer', 12)
#b.income()
a = Printer('Hp', 1500, 12, 'printer', 12)
print(a.my_print)








