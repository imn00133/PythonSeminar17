import random
side = int(input("면이 몇개? \n"))
while side==4 or side==6 or side==8 or side==12 or side==20:
    Userluck=random.randint(1,side)
    Comluck=random.randint(1,side)
    print("당신의 숫자는 %d 입니다." %Userluck)
    print("컴퓨터의 숫자는 %d 입니다." %Comluck)
    win=0
    trial=0
    if Userluck>Comluck:
        again=int(input("이겼습니다! 다시 하시겠습니까? 1:yes, 2:no \n"))
        win+=1
        trial+=1
        if again==1:
            print(" %d번 시도하여 %d번 승리하셨습니다!" %(trial,win))
            continue
        if again==2:
            print(" %d번 시도하여 %d번 승리하셨습니다! \n 수고하셨습니다." % (trial, win))
            break
    elif Userluck==Comluck:
        again=int(input(("비겼습니다! 다시 하시겠습니까? 1:yes, 2:no \n")))
        trial+=1
        if again==1:
            print(" %d번 시도하여 %d번 승리하셨습니다!" %(trial,win))
            continue
        if again==2:
            print(" %d번 시도하여 %d번 승리하셨습니다! \n 수고하셨습니다." % (trial, win))
            break
    else:
        again=int(input("졌습니다! 다시 하시겠습니까? 1:yes, 2:no \n"))
        trial+=1
        if again==1:
            print(" %d번 시도하여 %d번 승리하셨습니다!" % (trial, win))
            continue
        if again==2:
            print(" %d번 시도하여 %d번 승리하셨습니다! \n 수고하셨습니다." % (trial, win))
            break
if side!=4 or side!=6 or side!=8 or side!=12 or side!=20:
    print("정다면체의 면 수가 될 수 있도록 설정하세요")