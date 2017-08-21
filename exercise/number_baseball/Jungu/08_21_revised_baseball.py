import random
import copy
computer_list=[]
while 1:	
	user_number=int(input("숫자를 입력하세요: "))
	prototype=[0,1,2,3,4,5,6,7,8,9]
	strike=0
	ball=0
	out=0
	if user_number>=10 and user_number<10000000:
		if user_number>=10 and user_number<100:
			count=2
		elif user_number>=100 and user_number<1000:
			count=3
		elif user_number>=1000 and user_number<10000:
			count=4
		elif user_number>=10000 and user_number<100000:
			count=5
		elif user_number>=100000 and user_number<1000000:
			count=6
		elif user_number>=1000000 and user_number<10000000:
			count=7
		for a in range(0,count):
			computer_choice=random.choice(prototype)
			computer_list=computer_list+[computer_choice]
			prototype.remove(computer_choice)
		print(computer_list)
		for i in range(0,count):
			user_list=list(str(user_number))
			for j in range(0,count):
				if i!=j:
					if int(user_list[i])!=int(user_list[j]):
						pass
					else:
						print("다른 숫자를 입력하세요")	
						break
		for m in range(0,count):
			for n in range(0,count):
				if m==n:
					if int(user_list[m])==computer_list[n]:
						strike=strike+1
				else:
					if int(user_list[m])==computer_list[n]:
						ball=ball+1
		out=count-strike-ball
		print("strike: %s, ball: %s, out: %s" %(strike,ball,out))
		
	elif user_number>10000000:
		print("다시 입력하십시오")
	else:
		print("포기하셨습니다")
		break