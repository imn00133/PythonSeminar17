black=10
milk=10
luxury=10
while True:
    money = input("자판기에 돈을 넣으세요 : ")
    if money == "admin":
        while True:
            print("관리자 모드입니다.\n1.블랙커피: %d개\n2.밀크커피: %d개\n3.고급커피: %d개 남았습니다." % (black, milk, luxury))
            add = input("추가할 커피를 선택하세요(exit를 입력하면 종료됩니다.) : ")
            if add == "1":
                ba = int(input("추가할 블랙커피 개수를 입력하세요 : "))
                black = black + ba
            elif add == "2":
                ma = int(input("추가할 밀크커피 개수를 입력하세요 : "))
                milk = milk + ma
            elif add == "3":
                la = int(input("추가할 고급커피 개수를 입력하세요 : "))
                luxury = luxury + la
            elif add == "exit":
                print("관리자 모드를 끝냅니다.")
                break
            else:
                print("그런건 없습니다.")
    else:
        while True:
            money = int(money)
            choice = int(input("1. 블랙커피(100원)\n2. 밀크커피(150원)\n3. 고급커피(250원)\n4. 거스름돈\n선택하세요 : "))
            if choice == 1 and money >= 100 and black > 0:
                print("블랙커피\n돈이 %d원 남았습니다." % (money - 100))
                money = money - 100
                black = black - 1
            elif choice == 2 and money >=  150 and milk > 0:
                print("밀크커피\n돈이 %d원 남았습니다." % (money - 150))
                money = money - 150
                milk = milk - 1
            elif choice == 3 and money >= 250 and luxury > 0:
                print("고급커피\n돈이 %d원 남았습니다." % (money - 250))
                money = money - 250
                luxury = luxury - 1
            elif choice == 4:
                print("거스름돈 : " + str(money) + "원")
                exit()
            elif black == 0 or milk == 0 or luxury == 0:
                print("품절입니다.")
            elif choice not in [1, 2, 3, 4]:
                print("그런건 없습니다.")
            else:
                print("돈이 부족합니다." + "\n거스름돈 : " + str(money) + "원")
                break