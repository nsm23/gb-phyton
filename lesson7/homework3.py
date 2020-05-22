class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'теперь наша клетка = {(self.quantity + other.quantity)}'

    def __sub__(self, other):
        if int(self.quantity - other.quantity) < 0:
            return 'Клетка 1 должна быть больше клетки 2'
        else:
            return f'Наша клетка стала меньше: {self.quantity - other.quantity}'

    def __mul__(self, other):
        return f'Наша клетка увеличилась в {other.quantity} раз,' \
               f' и теперь равна: {(self.quantity * other.quantity)}'

    def __truediv__(self, other):
        try:
            return self.quantity // other.quantity

        except ZeroDivisionError:
            return f'Error other.quantity = 0'

    def make_order(self, row):
        self.row = int(row)
        quant = ''
        for i in range(int(self.quantity / row)):
            quant += 'o' * row + '\n'
        quant += 'o' * (self.quantity % row)
        return quant


c_1 = Cell(53)
c_2 = Cell(24)
print(f'Сложение: {c_1 + c_2}')
print(f'Вычитание: {c_1 - c_2}')
print(f'Деление: {c_1 / c_2}')
print(f'Умножение: {c_1 * c_2}')
print(c_1.make_order(13))
