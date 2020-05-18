class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} - Go!'

    def stop(self):
        return f'{self.name} - STOP.'

    def turn(self, direction):
        return f' {self.name} - turn {direction}'

    def show_speed(self):
        return f' speed - {self.speed}'


class TownCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 60:
            return 'Your speed exceeds 60 ml/h. Slow down speed.'
        else:
            return 'Your speed - normal.'


class WorkCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 40:
            return 'Your speed exceeds 40 ml/h. Slow down speed.'
        else:
            return 'Your speed - normal.'


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)


class SportCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)
        pass


city = TownCar('Maserati', 'black', 70, False)
print('Towncar: ' + city.go() + '\t\t' + city.show_speed() + '\t\t' + city.turn('Forward. ') + '\t\t' + city.stop())
print('**************************************************************************************************************')
village = WorkCar('Niva', 'white', 50, False)
print('Workcar: ' + village.go() + '\t\t\t' + village.show_speed() + '\t\t' + village.turn(
    'arround. ') + '\t\t\t' + village.stop())
print('**************************************************************************************************************')
race = SportCar('Lamborgini', 'yellow', 120, False)
print('SportCar: ' + race.go() + '\t' + race.show_speed() + '\t\t' * 5 + race.turn('left. ') + '\t\t' + race.stop())
print('**************************************************************************************************************')
police = PoliceCar('Ford', 'silver', 0, True)
print('Police: ' + police.go() + '\t\t\t' + police.show_speed() + '\t\t' * 5 + police.turn(
    'hid in the bushes. ') + '\t' + police.stop())
