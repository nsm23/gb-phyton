from time import sleep
import turtle


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        for i in range(len(TrafficLight.__color) + 2):
            if i == 0 or i == 4:
                print('\033[1m\033[031m Light - STOP!'.format())
                sleep(7)
            elif i == 1 or i == 3:
                print('\033[033m Light - GET READY...'.format())
                sleep(2)
            elif i == 2:
                print('\033[032m Light - GO-GO-GO!'.format())
                sleep(10)


traf = TrafficLight()
traf.running()
#___________________________________________________________________________________#
class Traffic_Light:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        turtle.setup(800, 600)
        turtle.hideturtle()
        turtle.pensize(6)
        turtle.circle(70)
        turtle.penup()
        turtle.goto(0, -140)
        turtle.pendown()
        turtle.circle(70)
        turtle.penup()
        turtle.goto(0, -280)
        turtle.pendown()
        turtle.circle(70)
        turtle.penup()
        for i in range(len(Traffic_Light.__color)):
            if i == 0:
                turtle.goto(0, 0)
                turtle.fillcolor(Traffic_Light.__color[i])
                turtle.begin_fill()
                turtle.circle(70)
                turtle.end_fill()
                turtle.penup()
                sleep(7)
            elif i == 1:
                turtle.goto(0, -140)
                turtle.begin_fill()
                turtle.fillcolor(Traffic_Light.__color[i])
                turtle.circle(70)
                turtle.end_fill()
                sleep(2)
            elif i == 2:
                turtle.goto(0, -280)
                turtle.begin_fill()
                turtle.fillcolor(Traffic_Light.__color[i])
                turtle.circle(70)
                turtle.end_fill()
                sleep(10)

a = Traffic_Light()
a.running()