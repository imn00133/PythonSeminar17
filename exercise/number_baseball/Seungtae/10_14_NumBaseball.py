import random

num=int(input("자리의 개수: "))

number=[0,1,2,3,4,5,6,7,8,9]
com_num=[]
user_num=[]
com_guess=[]
user_guess=[0,0,0,0,0,0,0,0,0,0,0,0,0]
str=0

def Match(arr1,arr2,num):
	ball=0
	strike=0
	for i in range(0,10):
		if arr1.count(i)==arr2.count(i) & arr1.count(i)==1:
			ball+=1
	for j in range(0,num):
		if arr1[j]==arr2[j]:
			strike+=1
	ball=ball-strike
	print("%d볼 %d스트라이크." %(ball,strike))
	return strike

random.shuffle(number)
com_num=number[0:num]
	
print(com_num)
while True:
	print("숫자를 입력하세요: ")
	for i in range(0,num):
		user_guess[i]=int(input())
	for j in range(0,num):
		print(user_guess[j],end=", ")
	print("")	
	str=Match(user_guess,com_num,num)
	if str==num:
		print("게임 끝!")
		break
	
print(com_num)