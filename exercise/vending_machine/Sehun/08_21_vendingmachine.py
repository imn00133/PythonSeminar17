while True:
	money = int(input("자판기에 돈을 넣으세요 : "))
	while True:
		choice = int(input("1. 블랙커피(100원)\n2. 밀크커피(150원)\n3. 고급커피(250원)\n4. 거스름돈\n선택하세요 : "))
		if choice == 1 and money < 100:
			print("돈이 부족합니다."+"\n거스름돈 : "+str(money)+"원")
			break
		elif choice == 1:
			print("블랙커피\n돈이 %d원 남았습니다." % (money-100))
			money = money-100
		elif choice == 2 and money < 150:
			print("돈이 부족합니다."+"\n거스름돈 : "+str(money)+"원")
			break
		elif choice == 2:
			print("밀크커피\n돈이 %d원 남았습니다." % (money-150))
			money = money-150
		elif choice == 3 and money < 250:
			print("돈이 부족합니다."+"\n거스름돈 : "+str(money)+"원")
			break
		elif choice == 3:
			print("고급커피\n돈이 %d원 남았습니다." % (money-250))
			money = money-250
		elif choice == 4:
			print("거스름돈 : "+str(money)+"원")
			break
		else:
			print("그런건 없습니다.")
	break