import turtle
import random

geobuk = turtle.Turtle()
radius = int(input("원의 크기를 정해주세요: "))
length = int(input("한번에 움직일 거리를 적어주세요: "))
geobuk.penup()
geobuk.sety(-radius)
geobuk.pendown()
geobuk.circle(radius)
geobuk.penup()
geobuk.sety(0)
geobuk.pendown()
while True:
    angle = random.randint(-180, 180)
    geobuk.right(angle)
    geobuk.forward(length)
    if geobuk.distance(0, 0) >= radius:
        break
