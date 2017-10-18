import turtle
import random
user=turtle.Turtle()
com=turtle.Turtle()
circ=turtle.Turtle()

def turn_right():
	user.setheading(0)
	user.forward(20)
def turn_up():
	user.setheading(90)
	user.forward(20)
def turn_left():
	user.setheading(180)
	user.forward(20)
def turn_down():
	user.setheading(270)
	user.forward(20)
def pen_up():
	user.penup()
def pen_down():
	user.pendown()
def blank():
	user.goto(0,0)
	user.clear()
def Chase(x,y):
	com.goto(x,y)
def Random():
	num=[1,2,3]
	number=random.choice(num)
	if number==1:
		angle=random.randint(-30,30)
		com.seth(angle)
		com.forward(20)
	else:
		pass
	return
		
com.speed(1)
com.penup()
com.setpos(-200,200)	
com.shape("circle")
com.shapesize(0.5,0.5,0.5)
com.fillcolor("red")
com.pencolor("red")
user.shape("turtle")
user.speed(10)
com.speed(1)
(a,b)=com.position()
circ.speed(0)
circ.penup()
circ.goto(0,-250)
circ.pendown()
circ.circle(250)
radius=250	
	
while True:
	(x,y)=user.position()
	user.screen.onkeypress(turn_right,"Right")
	user.screen.onkeypress(turn_left,"Left")
	user.screen.onkeypress(turn_up,"Up")
	user.screen.onkeypress(turn_down,"Down")
	user.screen.onkeypress(blank,"Escape")
	user.screen.onkeypress(pen_up,"space")
	user.screen.onkeyrelease(pen_down,"space")
	user.screen.listen()
	if x==a and y==b:
		break
	Chase(x,y)
	Random()
	(a,b)=com.position()
	radius-=2
	dist=user.distance(0,0)
	circ.penup()
	circ.goto(0,-radius)
	circ.pendown()
	circ.circle(radius)
	if dist>radius:
		break

print("게임 오버")