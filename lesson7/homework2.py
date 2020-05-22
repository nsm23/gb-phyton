class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    @property
    def total_area(self):
        return f'Всего необходимо {(self.size / 6.5 + 0.5) + (2 * self.height + 0.3):.2f}м. ткани.'


class Coat(Clothes):
    def __init__(self, size):
        super().__init__(size, height=0)

    def cons_coat(self):
        return f'Необходимо ткани на пошив пальто: {self.size / 6.5 + 0.5:.2f}м.'


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    def __str__(self):
        return f'Необходимо ткани на пошив костюма: {2 * self.height + 0.3:.2f}м.'


total = Clothes(42, 1.8)
coat = Coat(42)
suit = Suit(1.8)

print(coat.cons_coat() + '\n' + suit.__str__() + '\n\n' + total.total_area)
