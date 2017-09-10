import random
player1 = 0
player2 = 0
computer = 0
while True:
    gamechoice = int(input("게임을 선택하세요\n1. 주사위 게임\n2. 홀짝 게임\n3. 종료\n"))
    if gamechoice == 1:
        phase = int(input("주사위 면의 개수를 입력하세요 : "))
        if phase not in [4, 6, 8, 12, 20]:
            print("정다면체가 아닌데?")
        else:
            dice = int(input("던질 주사위의 개수를 입력하세요 : "))
            while True:
                a = []
                print("플레이어가 주사위를 던진 결과들 : ", end=" ")
                for i in range(1,dice+1):
                    a.append(random.randint(1, int(phase)))
                    print(a[i-1], end=" ")
                print("\n플레이어의 합 : " + str(sum(a)))
                b = []
                print("컴퓨터가 주사위를 던진 결과들 : ", end=" ")
                for i in range(1, dice + 1):
                    b.append(random.randint(1, int(phase)))
                    print(b[i - 1], end=" ")
                print("\n플레이어의 합 : " + str(sum(b)))
                if sum(a) > sum(b):
                    player1 = player1 + 1
                    print("플레이어가 이겻습니다!!!\n<전적>\n플레이어 : %d회\n컴퓨터 : %d회" % (player1, computer))
                elif sum(b) > sum(a):
                    computer = computer + 1
                    print("컴퓨터가 이겼습니다!!!\n<전적>\n플레이어 : %d회\n컴퓨터 : %d회" % (player1, computer))
                else:
                    print("비겼습니다!!!\n이긴 횟수\n플레이어 : %d회\n컴퓨터 : %d회" % (player1, computer))
                    if player1 > computer:
                        print("컴퓨터보다 우세합니다!!!")
                    elif player1 == computer:
                        print("막상막하!!!")
                    else:
                        print("지고있습니다!!!ㅋㅋㅋㅋㅋ")
                choice = input("다시 하시겠습니까? (Y : 재시작 / N : 끝내기)\n")
                if choice == "n" or choice == "N" :
                    print("주사위 게임을 끝냅니다.")
                    break
                elif choice == "y" or choice == "Y" :
                    print()
    elif gamechoice == 2:
        phase = int(input("주사위 면의 개수를 입력하세요 : "))
        if phase not in [4, 6, 8, 12, 20]:
            print("정다면체가 아닌데?")
        else:
            dice = int(input("던질 주사위의 개수를 입력하세요 : "))
            while True:
                c = []
                for i in range(1, dice + 1):
                    c.append(random.randint(1, int(phase)))
                destiny=input("컴퓨터가 주사위를 던졌습니다! 합이 홀인지 짝인지 맞추세요!\n당신의 선택은?! : ")
                if destiny == "홀":
                    if sum(c)%2 == 1:
                        print("주사위를 던진 결과 : ", end=" ")
                        for p in range(0, dice):
                            print(c[p], end=" ")
                        print("\n합계 : " + str(sum(c)) + "\n이겼습니다!")
                        player2 = player2 + 1
                    else:
                        print("주사위를 던진 결과 : ", end=" ")
                        for p in range(0, dice):
                            print(c[p], end=" ")
                        print("\n합계 : " + str(sum(c)) + "\n졌습니다!")
                elif destiny == "짝":
                    if sum(c)%2 == 0:
                        print("주사위를 던진 결과 : ", end=" ")
                        for p in range(0, dice):
                            print(c[p], end=" ")
                        print("\n합계 : " + str(sum(c)) + "\n이겼습니다!")
                        player2 = player2 + 1
                    else:
                        print("주사위를 던진 결과 : ", end=" ")
                        for p in range(0, dice):
                            print(c[p], end=" ")
                        print("\n합계 : " + str(sum(c)) + "\n졌습니다!")
                else:
                    print("엥? 문과이신가요? 홀짝중에서 고르세요!")
                print("지금까지 %d번 이겼습니다." % player2)
                choice = input("다시 하시겠습니까? (Y : 재시작 / N : 끝내기)")
                if choice == "n" or choice == "N" :
                    print("홀짝 게임을 끝냅니다.")
                    break
                elif choice == "y" or choice == "Y" :
                    print()
    elif gamechoice == 3:
        print("<전적>\n주사위 게임 : " + str(player1) + "회 승리" + "\n홀짝 게임 : " + str(player2) + "회 승리")
        break


