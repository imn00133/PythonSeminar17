import turtle
import random


def make_geobuk(color):
    geobuk = turtle.Turtle()
    geobuk.shape("turtle")
    geobuk.shapesize(1, 1, 2)
    geobuk.color("black", color)
    geobuk.penup()
    return geobuk


def chase_geobuk(geobuk):
    if random.randint(1, 5) == 3:
        geobuk.left(random.randint(0, 360))
    else:
        geobuk.seth(geobuk.towards(user_geobuk.position()))
    geobuk.forward(11)
#    if comp_geobuk.distance(user_geobuk.position()) < 10:
#        escape()


def release_key():
    user_geobuk.screen.onkeypress(up, "")
    user_geobuk.screen.onkeypress(down, "")
    user_geobuk.screen.onkeypress(left, "")
    user_geobuk.screen.onkeypress(right, "")
    user_geobuk.screen.onkeypress(escape, "Escape")


def on_key():
    user_geobuk.screen.onkeypress(up, "Up")
    user_geobuk.screen.onkeypress(down, "Down")
    user_geobuk.screen.onkeypress(left, "Left")
    user_geobuk.screen.onkeypress(right, "Right")
    user_geobuk.screen.onkeypress(escape, "Escape")


def up():
    user_geobuk.seth(90)


def down():
    user_geobuk.seth(270)


def left():
    user_geobuk.seth(180)


def right():
    user_geobuk.seth(0)


def escape():
    user_geobuk.screen.bye()


def play():
    on_key()
    release_key()
    user_geobuk.forward(10)
    chase_geobuk(comp_geobuk)
    user_geobuk.screen.ontimer(play, 100)


user_geobuk = make_geobuk("green")
comp_geobuk = make_geobuk("red")
user_geobuk.screen.listen()
play()
user_geobuk.screen.mainloop()