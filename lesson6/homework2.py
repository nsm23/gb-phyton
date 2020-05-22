class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def calculation(self):
        return self._length * self._width *25 # 25 - вес асфальта на 1кв. м. дороги

class Highway(Road):

    def __init__(self, _length, _width, depth):
        super().__init__(_length, _width)
        self.depth = depth
        #self.ves = 25
    def calculation(self):
        massa = Road.calculation(self) * self.depth# * self.ves
        return massa / 1000

ma = Highway(20, 5000, 5)
print('Нужно', format(ma.calculation(), ',.2f'), 'тонн асфальта')

#_________________________________________________________________________________________#
class Ro:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
        self.length = 25
        self.width = 5

    def calc(self):
        return self._length * self._width * self.length * self.width
massa_as = Ro(20, 5000)
print(massa_as.calc() / 1000)