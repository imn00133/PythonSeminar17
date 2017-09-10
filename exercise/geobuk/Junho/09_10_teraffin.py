import turtle
import random
junho=int(input("경계 원의 반지름을 정하세요 \n"))
turtle=turtle.Turtle()
turtle.shape('turtle')
turtle.right(90)
turtle.penup()
turtle.forward(junho)
turtle.left(90)
turtle.pendown()
turtle.circle(junho)
turtle.penup()
turtle.home()
turtle.pendown()
while True:
    youngcheon = random.randint(1, junho)
    turtle.forward(youngcheon)
    turtle.right(random.randint(1,360))
    jungu=turtle.distance(0, 0)
    if jungu>junho:
        break
    else:
        continue
