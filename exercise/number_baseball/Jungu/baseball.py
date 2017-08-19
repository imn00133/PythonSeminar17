import random
import copy

while 1:
	a=random.randint(0,9)
	b=random.randint(0,9)
	c=random.randint(0,9)
	d=random.randint(0,9)
	n2=[a,b,c,d]
	if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:
		break
	else:
		continue
while 1:
	y=input("숫자를 입력하세요")
	if int(y)<=9999 and int(y)>0:
		#내가 입력한 숫자와 컴퓨터가 뽑은 숫자를 리스트를 만듬
		t=list(y)
		y1=[int(t[0]),int(t[1]),int(t[2]),int(t[3])]
		#리스트에서 하나씩 비교
		strike=0
		n=copy.copy(n2)
		if n[0]==y1[0]:
			strike=strike+1
			n[0]="!"
			if n[1]==y1[1]:
				strike = strike + 1
				n[1]="!"
				if n[2]==y1[2]:
					strike=strike+1
					n[2]="!"
					if n[3]==y1[3]:
						strike=strike+1
						n[3]="!"
		elif n[1]==y1[1]:
			strike=strike+1
			n[1]="!"
			if n[2]==y1[2]:
				strike=strike+1
				n[2]="!"
				if n[3]==y1[3]:
					strike=strike+1
					n[3]="!"
		elif n[2]==y1[2]:
			strike=strike+1
			n[2]="!"
			if n[3]==y1[3]:
				strike=strike+1
				n[3]="!"
		elif n[3]==y1[3]:
			strike=strike+1
			n[3]="!"
		#볼,스트라이크,아웃 조건 맞추어서 개수 저장
		y2=set(y1)
		n1=set(n)
		ball=len(y2&n1)
		out=4-ball-strike
		print("strike %s, ball %s, out %s"%(strike,ball,out))
		if strike==4:
			break
	elif y>9999 :
		print("잘못 입력하셨습니다.")
	else:
		print("종료합니다.")
		break
		
	
	
		
	
