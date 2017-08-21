while True:
	phase = int(input("주사위 면의 개수를 입력하세요 : "))
	if phase in [4, 6, 8, 12, 20]:
		박세훈 = 2
		while 박세훈 >= 0:
			if 박세훈 == 2:
				dice1 = int(input("플레이어가 던질 주사위의 개수를 입력하세요 : "))
				a=[]
				while dice1 > 0:
					a.append(random.randint(1,int(phase)))
					dice1 = dice1-1
				print("플레이어가 주사위를 던진 결과의 리스트 : "+str(a)+"\n"+"플레이어의 합 : "+str(sum(a)))
				박세훈 = 박세훈-1
			elif 박세훈 == 1:
				dice2 = int(input("컴퓨터가 던질 주사위의 개수를 입력하세요 : "))
				b=[]
				while dice2 > 0:
					b.append(random.randint(1,int(phase)))
					dice2 = dice2-1
				print("컴퓨터가 주사위를 던진 결과의 리스트 : "+str(b)+"\n"+"컴퓨터의 합 : "+str(sum(b)))
				박세훈 = 박세훈-1
			elif 박세훈 == 0:
				if sum(a) > sum(b):
					print("플레이어가 이겻습니다!!!")
				elif sum(b) > sum(a):
					print("컴퓨터가 이겼습니다!!!")
				else:
					print("비겼습니다!!!")
				박세훈 = 박세훈-1
	else:
		print("정다면체가 아닌데?")