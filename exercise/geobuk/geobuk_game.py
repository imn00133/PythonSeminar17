import turtle
import random


def make_geobuk(color):
    geobuk = turtle.Turtle()
    geobuk.shape("turtle")
    geobuk.shapesize(1, 1, 2)
    geobuk.color("black", color)
    geobuk.penup()
    return geobuk


def chase_geobuk():
    if random.randint(1, 5) == 3:
        comp_geobuk.left(random.randint(0, 360))
    else:
        comp_geobuk.seth(comp_geobuk.towards(user_geobuk.position()))
    comp_geobuk.forward(11)
#    if comp_geobuk.distance(user_geobuk.position()) < 10:
#        escape()


def up():
    user_geobuk.seth(90)
    user_geobuk.forward(10)
    chase_geobuk()


def down():
    user_geobuk.seth(270)
    user_geobuk.forward(10)
    chase_geobuk()


def left():
    user_geobuk.seth(180)
    user_geobuk.forward(10)
    chase_geobuk()


def right():
    user_geobuk.seth(0)
    user_geobuk.forward(10)
    chase_geobuk()


def escape():
    user_geobuk.screen.bye()


user_geobuk = make_geobuk("green")
comp_geobuk = make_geobuk("red")
user_geobuk.screen.onkeypress(up, "Up")
user_geobuk.screen.onkeypress(down, "Down")
user_geobuk.screen.onkeypress(left, "Left")
user_geobuk.screen.onkeypress(right, "Right")
user_geobuk.screen.onkeypress(escape, "Escape")
user_geobuk.screen.listen()
user_geobuk.screen.mainloop()