class Complex:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def __add__(self, other):
        return f'Complex summa = {self.num1 + other.num1} + {self.num2 + other.num2} *i'

    def __mul__(self, other):
        return f'Complex product = {self.num1 * other.num1} - {self.num2 * other.num2} * i'


a = Complex(5, 9)
b = Complex(4, 3)
print(a + b)
print(a * b)
