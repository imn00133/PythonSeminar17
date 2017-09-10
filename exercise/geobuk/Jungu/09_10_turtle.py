import random
import turtle

dot = turtle.Turtle
dot.shapesize(3, 2, 1)
dot.shape(classic)
while 1:
    angle = random.randint(1, 360)
    dot.right(angle)
    dot.forward(1)
