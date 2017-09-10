import turtle
import random


def circle(turtle, length):
    """
    거북이 원 그리는 함수
    :param turtle: 돌릴 거북이 객체
    :param length: 원의 길이
    """
    if turtle.isdown():
        turtle.penup()
    turtle.forward(length)
    turtle.setheading(90)
    turtle.pendown()
    turtle.circle(length)
    turtle.penup()
    turtle.home()
    turtle.pendown()

geobuk = turtle.Turtle()
geobuk.shape("turtle")
geobuk.shapesize(2, 2, 3)

circle_len = int(input("원의 크기를 입력하세요: "))
turtle_forward = int(input("거북이가 움직일 거리를 입력하세요: "))
circle(geobuk, circle_len)

# 랜덤으로 돌면서 움직이기
while geobuk.distance(0, 0) <= circle_len:
    geobuk.left(random.randint(0, 360))
    geobuk.forward(turtle_forward)

geobuk.screen.mainloop()
