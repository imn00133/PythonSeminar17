# 거북이모듈
## 17.09.04
turtle모듈을 사용하여 사용자가 입력한 크기의 원을 그린다. 그 후 사용자가 입력한 길이만큼 직진-> 랜덤으로 거북이가 도는 것을 반복한다. 이 때, 사용자가 입력한 크기의 원을 벗어나면 거북이가 멈추고 종료하도록 만든다.

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
