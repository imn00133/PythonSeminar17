import turtle
import random
import copy

turtle = turtle.Turtle()
turtle.speed(5)
Diameter = int(input("Circle Diameter: "))
turtle.penup()
turtle.right(90)
turtle.forward(Diameter)
turtle.pendown()
turtle.left(90)
turtle.circle(Diameter)
turtle.penup()
turtle.home()
turtle.pendown()
TurtleEnd = 0
while 1:
    UserLength = input("Forward(Num or End): ")
    if UserLength == 'End':
        TurtleEnd = 1
        break
    else:
        UserLength = int(UserLength)
    turtle.forward(UserLength)
    (x, y) = turtle.position()
    if x*x + y*y > Diameter*Diameter:
        turtle.undo()
        Forward = copy.deepcopy(UserLength)
        while 1:
            Forward = Forward/2
            if Forward > 1:
                turtle.forward(Forward)
            else:
                turtle.forward(1)
            (x, y) = turtle.position()
            if x*x + y*y > Diameter*Diameter and Forward >= 1:
                turtle.undo()
            elif x*x + y*y > Diameter*Diameter and Forward <= 1:
                turtle.undo()
                TurtleEnd = 1
                break
    if TurtleEnd == 1:
        break
    Heading = random.randint(0, 360)
    turtle.right(Heading)
turtle.screen.mainloop()