user_number=int(input("숫자를 입력하세요: "))
for i in range(1,user_number+1):
	log=0
	double=0
	triple=0
	number_list=list(str(i))
	for j in range(0,user_number):
		if i//(10**j)>=1:
			log=log+1
		else:
			pass
	for a in range(0,log):
		if int(number_list[a])==3 or int(number_list[a])==6 or int(number_list[a])==9:
			triple=triple+1
	for b in range(0,log):
		if int(number_list[b])==2 or int(number_list[b])==4 or int(number_list[b])==6 or int(number_list[b])==8:
			double=double+1
	if double!=0 or triple!=0:
		print("뽕"*double+"짝"*triple, end=' ')
	else:
		print(i, end=' ')
	if i%20==0:
		print(" ")