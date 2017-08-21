import random
import copy
user_number=int(input("실행횟수를 입력하세요: "))
montihall_number=int(input("문의 개수를 입력하세요: "))
open=int(input("열고 싶은 문의 수를 결정하시오: "))
montihall_list=[]
loop=1
correct1=0
correct2=0
loading_number=0
for i in range(0,montihall_number):
	montihall_list=montihall_list+[i]
while loop<=user_number:
	loop=loop+1
	answer=random.choice(montihall_list)
	choice=random.choice(montihall_list)
	prototype=copy.copy(montihall_list)
	if answer!=choice:
		prototype.remove(answer)
		prototype.remove(choice)
		for m in range(0,open):
			removed_choice=random.choice(prototype)
			prototype.remove(removed_choice)
		prototype.append(answer)
		revised_choice=random.choice(prototype)
	else:
		prototype.remove(answer)
		for n in range(0,open):
			removed_choice=random.choice(prototype)
			prototype.remove(removed_choice)
		prototype.append(answer)	
		revised_choice=random.choice(prototype)
	if answer==choice:
		correct1=correct1+1
	elif answer==revised_choice:
		correct2=correct2+1
	loading=loading_number/user_number
	print("로딩중: %.2f%%" %(loading*100))
	loading_number=loading_number+1
first_probablity=correct1/user_number
second_probablity=correct2/user_number
print("선택을 바꾸었을 경우: %s, 선택을 바꾸지 않을 경우: %s" %(second_probablity,first_probablity))