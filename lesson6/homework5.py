class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки.'


class Pen(Stationary):
    def draw(self):
        return f'{self.title}  - запуск отрисовки.'


class Pencil(Stationary):
    def draw(self):
        return f'{self.title} - запуск отрисовки.'

class Handly(Stationary):
    def draw(self):
        return f'{self.title} - запуск отрисовки'

pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handly = Handly('Маркер')
print(pen.draw(), pencil.draw(), handly.draw(), sep='\n')



