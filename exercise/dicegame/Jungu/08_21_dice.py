import random
game=0
win=0
regame=1
while 1:	
	user_number=int(input("정다면체의 면의 개수를 입력하시오: "))
	dice=int(input("주사위의 개수를 입력하시오: "))
	sum_of_dice=0
	sum_of_dice_computer=0
	if user_number==4 or user_number==6 or user_number==8 or user_number==12 or user_number==20:
		while regame:
			sum_of_dice=0
			sum_of_dice_computer=0
			game=game+1
			for j in range(1,dice+1):	
				dice_number=[]
				for i in range(1,user_number+1):
					dice_number=dice_number+[i]
				random_number=random.choice(dice_number)
				random_number_computer=random.choice(dice_number)
				print("사용자의 %s번쨰 주사위의 눈금: %s" %(j,random_number))
				print("컴퓨터의 %s번째 주사위의 눈금: %s" %(j,random_number_computer))
				sum_of_dice=sum_of_dice+random_number
				sum_of_dice_computer=sum_of_dice_computer+random_number_computer
				if j==dice:
					print("사용자의 주사위 눈금의 총 합: %s" %sum_of_dice)
					print("컴퓨터의 주사위 눈금의 총 합: %s" %sum_of_dice_computer)
					if sum_of_dice>sum_of_dice_computer:
						win=win+1
						print("사용자가 이겼습니다.")
						print("현재까지 %s판 중 %s판 이겼습니다."  %(game,win))
					elif sum_of_dice==sum_of_dice_computer:
						print("비겼습니다.")
					else:
						print("컴퓨터가 이겼습니다.")
			regame= int(input("다시 하시겠습니까?(1=예,0=아니오): "))
				
	else:
		print("다시 입력하시오")