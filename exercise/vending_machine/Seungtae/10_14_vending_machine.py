def Stock():
	f=open("stock.txt",'r',encoding='utf-8')
	stock=f.readlines()
	for i in range(0,len(stock)):
		stock[i]=stock[i].split()
	print(stock)
	f.close()
	return stock
	
def Write(stock):
	f=open("stock.txt",'w',encoding='utf-8')
	for i in range(0,len(stock)):
		f.write(kind[i]+" "+str(price[i])+" "+str(amount[i]))
		f.write("\n")
	f.close()
	return stock
money=0
while True:
	stock=Stock()
	kind=[]
	price=[]
	amount=[]
	for i in range(0,len(stock)):
		kind.append(stock[i][0])
		price.append(int(stock[i][1]))
		amount.append(int(stock[i][2]))
	for j in range(0,len(stock)):
		print("%d.%s:%d원" %(j+1,kind[j],price[j]), end=' ')
	print("%d.거스름돈 반환" %(len(stock)+1))	
	print("현재 금액은 %d입니다." %money)
	monint=money
	money=input("돈을 투입하세요.: ")
	if money=="admin":
		print("")
		print("="*20)
		print("{0:^15}".format("관리자입니다."))
		print("="*20)
		print("")
		for i in range(0,len(stock)):
			print("%d.%s의 양은 %d," %(i+1,kind[i],amount[i]), end=' ')
		print("%d.새로운 커피 추가" %(len(stock)+1))
		money=monint
		add=input("\n어떤 커피를 추가하시겠습니까.: ")
		if add=="exit":
			print("나갑니다.\n")		
		else:
			add=int(add)-1
			if add in range(0,len(stock)):
				cofnum=int(input("얼마나 추가하시겠습니까: "))
				amount[add]+=cofnum
				Write(stock)
			elif add==len(stock):
				kind_add=input("추가할 커피의 이름은?: ")
				price_add=input("그 커피의 가격은?: ")
				amount_add=input("그 커피의 양은?: ")
				add_add=kind_add+" "+price_add+" "+amount_add
				f=open("stock.txt",'a',encoding='utf-8')
				f.write("\n")
				f.write(add_add)
				f.close()
			else:
				print("그런 커피는 없습니다.\n")
	else:
		money=int(money)
		money=monint+money
		num=int(input("무엇을 드시려고: "))-1
		if num in range(0,len(stock)):
			if money>=price[num] and amount[num]>0:
				print("%s가 나오는 중입니다.\n" %kind[num])
				money-=price[num]
				amount[num]-=1
				num=0
			elif money<price[num]:
				print("돈이 부족합니다.\n")
			else:
				print("품절입니다.\n")
		elif num==len(stock):
			print("거스름돈은 %d입니다." %money)
			break
		else:
			print("메뉴에 없는 주문입니다.\n")