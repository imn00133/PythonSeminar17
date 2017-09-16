# 거북이모듈
## 17.09.04
turtle모듈을 사용하여 사용자가 입력한 크기의 원을 그린다.
그 후 사용자가 입력한 길이만큼 직진-> 랜덤으로 거북이가 도는 것을 반복한다.
이 때, 사용자가 입력한 크기의 원을 벗어나면 거북이가 멈추고 종료하도록 만든다.

거북이 사용하기
import turtle
turtle=turtle.Turtle()

거북이 모듈 함수
turtle.shape('shape') 거북이 모양을 바꾼다. turtle, arrow, circle, square, triangle, classic으로 6가지가 있다.
turtle.shapesize(y, x, outline) 세로로 y배, 가로로 x배, 윤곽선은 outline배를 한다.
turtle.forward(distance) distance만큼 움직인다.
turtle.backward(distance) distance만큼 뒤로 움직인다.
turtle.right(angle) angle만큼 오른쪽으로 돈다.
turtle.left(angle) angle만큼 왼쪽으로 돈다.
turtle.setheading(angle) 오른쪽(0)을 기준으로 고정된 각도를 본다. 위쪽(90) 왼쪽(180) 아래쪽(270)
turtle.goto(x, y) 중앙을 0,0으로 잡아 x, y만큼 이동한다.
turtle.setx(x) 중앙을 0,0으로 잡고 x만큼 이동한다.
turtle.sety(y) 중앙을 0,0으로 잡고 y만큼 이동한다.
turtle.circle(distance) 거북이가 있는 위치에서 반시게 방향으로 distance크기의 원을 그린다.
turtle.home() 화면 중심으로 돌아오고, 방향도 초기상태인 우측으로 바뀐다.
turtle.clear() 모든 선을 지운다.
turtle.undo() 바로 직전에 수행한 작업을 취소한다.
turtle.speed(num) 거북이의 속도를 조절한다.0-10까지 가능하며, 10보다 크거나 0.5보다 작으면 0으로 고정된다. 정해진 문자열을 넣어도 된다.
“fastest”: 0
“fast”: 10
“normal”: 6
“slow”: 3
“slowest”: 1
// 그리는 속도를 말하기 때문에, 1이 가장 느리고, 10이 가장 빠르다. 0은 애니메이션을 그리지 않는다.

turtle.position() 위치를 반환해준다.
turtle.heading() 보는 방향을 반환해준다.
turtle.distance(x,y) x,y의 좌표와 현재 위치 사이의 거리를 반환한다.

turtle.pendown() 펜을 내린다.
turtle.penup() 펜을 올린다.
turtle.isdown() 펜이 내려와있으면 True, 올라가있으면 False를 반환한다.

PyCharm에서 그래픽이 종료될 때, 맨 마지막에 turtle.screen.mainloop()를 넣어주면 된다.

python reference https://docs.python.org/3/library/turtle.html
자주 사용하는 메소드(한글) https://blog.naver.com/javaking75/220740422160

## 17.09.16
거북이 모듈 게임
두 마리 거북이를 만들고, 하나의 거북이는 사람이 조종할 수 있도록 만들고 하나의 거북이는 컴퓨터가 조종하도록 만든다.
두 거북이는 랜덤한 위치에 있으나, 양쪽의 거리는 200px이상의 거리를 가지도록 한다.
사람의 조정하는 거북이를 컴퓨터가 따라오도록 만들고, 둘이 겹치면 프로그램이 종료되도록 한다.
단, 컴퓨터의 이동거리는 사람이 조정하는 거북이의 이동거리보다는 길지만, 게임의 재미를 위해 3-5번 이동시 컴퓨터가 조종하는 거북이는 사람이 조정하는 거북이를 따라가는 것이 아니라 랜덤한 방향으로 이동하게 만든다.

거북이 모듈 함수
거북이설정 함수
turtle.shape('shape') 거북이 모양을 바꾼다. turtle, arrow, circle, square, triangle, classic으로 6가지가 있다.
turtle.shapesize(y, x, outline) 세로로 y배, 가로로 x배, 윤곽선은 outline배를 한다.
turtle.speed(num) 거북이의 속도를 조절한다.0-10까지 가능하며, 10보다 크거나 0.5보다 작으면 0으로 고정된다. 정해진 문자열을 넣어도 된다.
“fastest”: 0
“fast”: 10
“normal”: 6
“slow”: 3
“slowest”: 1
// 그리는 속도를 말하기 때문에, 1이 가장 느리고, 10이 가장 빠르다. 0은 애니메이션을 그리지 않는다.
turtle.screen.title("title") 거북이창의 타이틀을 바꾼다.

이동관련 함수
turtle.forward(distance) or turtle.fd(distance) distance만큼 움직인다.
turtle.backward(distance) or turtle.back(distance) distance만큼 뒤로 움직인다.
turtle.goto(x, y) or turtle.setpos(x, y) 중앙(0,0)을 기준으로 x, y만큼 이동한다.
turtle.setx(x) 중앙(0,0)을 기준으로 x만큼 이동한다.
turtle.sety(y) 중앙(0,0)을 기준으로 y만큼 이동한다.
turtle.circle(distance) 거북이가 있는 위치에서 반시게 방향으로 distance크기의 원을 그린다.

회전관련 함수
turtle.right(angle) or turtle.rt(angle) angle만큼 오른쪽으로 돈다.
turtle.left(angle) or turtle.lt(angle) angle만큼 왼쪽으로 돈다.
turtle.setheading(angle) or turtle.seth(angle) 오른쪽(0)을 기준으로 고정된 각도를 본다. 위쪽(90) 왼쪽(180) 아래쪽(270)
turtle.heading() 현재 바라보는 각도를 반환한다.
turtle.toward(x, y) 현재 거북이가 있는 위치에서 특정 위치까지 바라보는 각도를 구한다.

초기화관련 함수
turtle.home() 화면 중심으로 돌아오고, 방향도 초기상태인 우측으로 바뀐다.
turtle.clear() 거북이를 그대로 둔 채, 모든 선을 지운다.
turtle.reset() 거북이를 원래로 되돌리며, 화면을 지운다.
turtle.undo() 바로 직전에 수행한 작업을 취소한다.

위치 관련 함수
turtle.position() 위치를 반환해준다.
turtle.heading() 보는 방향을 반환해준다.
turtle.distance(x,y) x,y의 좌표와 현재 위치 사이의 거리를 반환한다.
turtle.xcor() x좌표를 구한다.
turtle.ycor() y좌표를 구한다.

펜 관련 함수
turtle.pendown() or turtle.down() 펜을 내린다.
turtle.penup() or turtle.up 펜을 올린다.
turtle.isdown() 펜이 내려와있으면 True, 올라가있으면 False를 반환한다.
turtle.pensize(width) or turtle.width(width) width의 굵기로 그린다.

채우기 관련 함수
turtle.begin_fill() 도형 내부를 색칠할 준비를 한다.
turtle.end_fill() begin_fill() 이후 지금까지 그린 그림에 맞춰 내부를 색칠한다.
turtle.filling() turtle.begin_fill()을 시작했는지 알려준다. begin_fill()을 실행했을 경우 True를 반환하고 아니면 False를 반환한다.

표시 관련 함수
turtle.showturtle() or turtle.st() 거북이를 화면에 표시한다.
turtle.hideturtle() or turtle.ht() 거북이를 화면에서 가린다.
turtle.isvisible() 거북이가 보이면 True를 반환한다.

색 관련 함수
turtle.screen.bgcolor("color") 화면의 배경색을 바꾼다.
turtle.pencolor("color") color로 펜 색을 바꾼다. 또한, 거북이 윤곽선 색이 바뀐다.
turtle.fillcolor("color") color로 채운다. 또한, 거북이 내부색이 바뀐다.
turtle.color() 펜 색과 채우기 색을 반환한다.
turtle.color("color1") 펜 색을 color1으로 바꾼다.
turtle.screen.color("color1", "color2") 펜 색을 color1, 채우기 색을 color2로 바꾼다.
"color"에 들어갈 수 있는 색은 "color list의 이름"이나 ""#285078"와 같이 16진수 rgb값으로 들어갈 수 있다.
또는 "color"대신 (r, g, b)나 r, g, b가 들어갈 수 있다. ex) turtle.pencolor((25, 30, 5))==turtle.pencolor(25, 30, 5)
이 때, r, g, b에 들어갈 수 있는 값은 1.0까지의 값이나 255까지의 값이다. 기본값은 1.0이 최대인 값이다.
turtle.colormode(1.0 or 255) r, g, b에 들어갈 수 있는 값을 1.0을 최대로 하거나 255를 최대로 만들 수 있다. 기본값은 1.0이다

사용 가능 색 list로 보인다.
https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm
PyCharm에서 그래픽이 종료될 때, 맨 마지막에 를 넣어주면 된다.

입력이 있을 때 함수를 호출하는 함수
turtle.screen.onkeyrelease(function, "key") "key"를 때면 function을 호출한다.
turtle.screen.onkeypress(function, "key") "key"를 누르면 function을 호출한다. (방향키 위("Up"), 왼쪽("left"), esc("Escape"), space("space")등)
turtle.screen.onscreenclick(function) 마우스 버튼을 눌렀을 때 fucntion을 호출한다. (turtle.screen.onscreenclick(turtle.goto)는 거북이를 마우스 버튼을 누른 위치로 이동시킨다.)
turtle.screen.ontimer(function, time) time(ms)후에 fuction을 호출한다.
turtle.screen.listen() 사용자 입력이 처리되도록 거북이 그래픽창에 포커스를 준다.
turtle.screen.mainloop() mainloop로 들어가서 사용자 입력을 받도록 한다.
더 많은 함수는 https://docs.python.org/3/library/turtle.html

글씨출력 함수
turtle.write("string", move=False, align="left", font=("Arial", 8, "normal")) 현재 거북이 위치에 "string"을 출력한다.
move는 글씨의 끝으로 거북이를 움직이게 한다. 색은 거북이 펜색이다.
align 정렬(left, center, right)
ex) turtle.write("String", False, "center", ("",20)) 현재 거북이 위치에 가운데 정렬로 크기가 20인 글씨를 쓴다.

종료 함수
turtle.screen.bye()
