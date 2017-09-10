bc = 5
mc = 5
pc = 5
while 1:
    money = input("돈을 입력하세요: ")
    if money == "admin":
        while 1:
            print("블랙커피:%s, 밀크커피:%s, 고급커피:%s" % (bc, mc, pc))
            recharge = input("추가할 커피를 선택하시오-1:블랙커피,2:밀크커피,3:고급커피,4:exit: ")
            if int(recharge) == 1:
                plus_bc = int(input("추가할 블랙커피의 양을 정하시오:"))
                bc = bc + plus_bc
            elif int(recharge) == 2:
                plus_mc = int(input("추가할 밀크커피의 양을 정하시오:"))
                mc = mc + plus_mc
            elif int(recharge) == 3:
                plus_pc = int(input("추가할 고급커피의 양을 정하시오:"))
                pc = pc + plus_pc
            elif int(recharge) == 4:
                break
    elif int(money) >= 100:
        money = int(money)
        print("1.블랙커피:100원, 2.밀크커피:150원, 3.고급커피:250원")
        choice = int(input("커피를 선택하세요"))
        if choice == 1:
            if money >= 100 and bc > 0:
                money = money - 100
                bc = bc - 1
                print("블랙커피를 선택했습니다. 거스름돈은 %s원 입니다." % money)

        elif choice == 2:
            if money >= 150 and mc > 0:
                money = money - 150
                mc = mc - 1
                print("밀크커피를 선택했습니다. 거스름돈은 %s원 입니다." % money)

            else:
                print("선택할 수 없습니다.")
                print("거스름돈은 %s 입니다." % money)

        elif choice == 3:
            if money >= 250 and pc > 0:
                money = money - 250
                pc = pc - 1
                print("고급커피를 선택했습니다. 거스름돈은 %s원 입니다." % money)

            else:
                print("선택할 수 없습니다.")
                print("거스름돈은 %s원 입니다." % money)

    elif int(money) < 100:
        print("돈이 부족합니다")
        print("거스름돈은 %s원 입니다." % money)
        break
