import turtle
import random

move = 0
def turn_right():
    user.setheading(0)
    user.forward(20)
    global move
    move = move + 1
    chase()
    i_got_you()
def turn_up():
    user.setheading(90)
    user.forward(20)
    global move
    move = move + 1
    chase()
    i_got_you()
def turn_left():
    user.setheading(180)
    user.forward(20)
    global move
    move = move + 1
    chase()
    i_got_you()
def turn_down():
    user.setheading(270)
    user.forward(20)
    global move
    move = move + 1
    chase()
    i_got_you()
def blank():
    user.clear()
def chase():
    global move
    if move % 3 == 0:
        computer.seth(random.randint(0,360))
        computer.forward(15)
    else:
        (a,b) = user.position()
        angle1 = computer.towards(a,b)
        angle2 = computer.heading()
        computer.left(angle1 - angle2)
        computer.forward(30)
def i_got_you():
    (a,b) = user.position()
    (c,d) = computer.position()
    if (a-c)**2 + (b-d)**2 <= 100:
        exit()
computer=turtle.Turtle()
computer.fillcolor("red")
computer.speed(5)
computer.shape("turtle")
user = turtle.Turtle()
user.fillcolor("blue")
user.speed(0)
user.shape("turtle")
while 1:
    a=random.randint(-300,300)
    b=random.randint(-300,300)
    c=random.randint(-300,300)
    d=random.randint(-300,300)
    if (a-c)**2+(b-d)**2 >= 40000:
        computer.penup()
        computer.goto(a,b)
        user.penup()
        user.goto(c,d)
        break
    else:
        pass

user.screen.onkeypress(turn_right, "Right")
user.screen.onkeypress(turn_up, "Up")
user.screen.onkeypress(turn_left, "Left")
user.screen.onkeypress(turn_down, "Down")
user.screen.onkeypress(blank, "Escape")
user.screen.listen()
user.screen.mainloop()


#towards로 좌표 받아쓰기