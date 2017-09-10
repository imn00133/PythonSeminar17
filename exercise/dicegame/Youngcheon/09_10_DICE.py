import random
import os

#게임 함수 1. 합계 게임
def SumGame(FaceNum, NumofDice):
    global WinNumSUM
    WinNumSUM = 0
    while 1:
        os.system("cls")
        #컴터가 주사위를 굴려 얻는 숫자와 합계
        ComList = []
        ComSum = 0
        print("Computer: ", end="")
        for i in range(0, NumofDice):
            ComDice = random.randint(1, FaceNum)
            ComList.append(ComDice)
            ComSum += ComDice
            if i == NumofDice -1:
                print(ComDice, end= "   ")
            else:
                print(ComDice, end= ", ")
        print("Sum: %d" %ComSum)
        #유저가 주사위를 굴려 얻는 숫자와 합계 (ctrl+C, ctrl+v 후 변수만 바꿈)
        Userlist = []
        Usersum = 0
        print("User: ", end="")
        for i in range(0, NumofDice):
            Userdice = random.randint(1, FaceNum)
            Userlist.append(Userdice)
            Usersum += Userdice
            if i == NumofDice -1:
                print(Userdice, end= "   ")
            else:
                print(Userdice, end= ", ")
        print("Sum: %d" %Usersum)
        #합계 비교 후 결과
        if ComSum > Usersum:
            print("User LOSE")
        elif ComSum == Usersum:
            print("DRAW")
        else:
            WinNumSUM += 1
            print("User WIN %d time(s)" %WinNumSUM)
        #다시하기 / 이게임 끝내기 / 주사위 바꾸기
        while 1:
            UserTry = input("Retry? (yes / no / change)\n")
            global Result
            #이게임 끝내기 - return 값은 사용하지 않지만 break와 똑같은 역할
            if UserTry == "no":
                Result = "No"
                return (Result, WinNumSUM)
            #이게임 다시하기 - 질문 다시받는 while 문만 나가면 다시 시작
            elif UserTry == "yes":
                break
            #이게임 주사위 바꾸기 - 전역변수 Result를 이용함, returm은 break와 동일
            elif UserTry == "change":
                Result = "Change"
                return (Result, WinNumSUM)
            else:
                continue

#게임함수 2. 홀짝 게임
def EvenOddGame(FaceNum, NumofDice):
    global WinNumOE
    WinNumOE = 0
    while 1:
        os.system("cls")
        #컴터가 주사위를 굴려 얻는 수 (이것또한 복붙 후 변수명 수정)
        ComList = []
        ComSum = 0
        UserChoice = input("ODD / EVEN\n")
        print("Computer: ", end="")
        for i in range(0, NumofDice):
            ComDice = random.randint(1, FaceNum)
            ComList.append(ComDice)
            ComSum += ComDice
            if i == NumofDice -1:
                print(ComDice, end= "   ")
            else:
                print(ComDice, end= ", ")
        if ComSum%2 == 0:
            ComOE = "EVEN"
        else:
            ComOE = "ODD"
        print("Sum: %d(%s)" %(ComSum, ComOE))
        #컴터 홀짝과 유저 홀짝은 같은가
        if ComOE != UserChoice:
            print("User LOSE")
        else:
            WinNumOE += 1
            print("User WIN %d time(s)" %WinNumOE)
        #게임 1에서와 똑같은 방식
        while 1:
            UserTry = input("Retry? (yes / no / change)\n")
            global Result
            if UserTry == "no":
                Result = "No"
                return (Result, WinNumOE)
            elif UserTry == "yes":
                break
            elif UserTry == "change":
                Result = "Change"
                return (Result, WinNumOE)
            else:
                continue

#3. 주사위 듀얼 게임
def DiceDual(FaceNum, NumofDice):
    global WinNumDD
    WinNumDD = 0
    while 1:
        ComHealth = 100
        print("ComeHealth : %d" %ComHealth)
        UserHealth = 100
        print("UserHealth: %d" %UserHealth)
        ComSum = 0
        UserSum = 0
        for i in range(0, NumofDice):
            ComDice = random.randint(1, FaceNum)
            ComSum = ComSum + ComDice
        print("Computer Sum: %d" %ComSum)
        for i in range(0, NumofDice):
            UserDice = random.randint(1, FaceNum)
            UserSum = UserSum + UserDice
        print("User Sum: %d" %UserSum)
        if ComSum == UserSum:
            pass
        elif ComSum < UserSum:
            ComHealth = ComHealth - (UserSum - ComSum)
        else:
            UserHealth = UserHealth - (ComSum - UserSum)
        print("ComeHealth : %d" %ComHealth)
        print("UserHealth: %d" %UserHealth)
        while 1:
            UserTry = input("Retry? (yes / no / change)\n")
            global Result
            if UserTry == "no":
                Result = "No"
                if UserHealth == ComHealth:
                    pass
                elif UserHealth < ComHealth:
                    pass
                else:
                    WinNumDD = WinNumDD +1
                return (Result, WinNumDD)
            elif UserTry == "yes":
                break
            elif UserTry == "change":
                Result = "Change"
                if UserHealth == ComHealth:
                    pass
                elif UserHealth < ComHealth:
                    pass
                else:
                    winNumDD = winNumDD +1
                return (Result, WinNumDD)
            else:
                continue

#주사위 면 & 개수 설정
def DICE():
    while 1:
        global DiceFaceNum
        global DiceNum
        DiceFaceNum = int(input("Number of Dice Faces : "))
        if DiceFaceNum != 4 and DiceFaceNum != 6 and DiceFaceNum != 8 and DiceFaceNum != 12 and DiceFaceNum != 20:
            continue
        DiceNum = int(input("Number of Dices: "))
        break
    os.system("cls")

#주사위 게임 프로그램 목록
SumTotalWin = 0
OETotalWin = 0
DDTotalWin = 0
Result = "Change"
while 1:
    os.system("cls")
    #처음 혹은 주사위를 바꾸고 싶을때
    if Result =="Change":
        DICE()
    #아니면 뭐 그냥 진행
    print('''DICE RELATED GAME SERIES
    
    1. DICE SUM GAME
    2. DICE EVENNESS GAME
    3. DICE DUAL GAME
    4. Exit
    
    ''')
    GameNum = input("CHOICE: ")
    os.system("cls")
    if GameNum == '1':
        SumGame(DiceFaceNum, DiceNum)
        if Result == "Change":
            SumTotalWin += WinNumSUM
            os.system("cls")
            continue
        elif Result == "No":
            SumTotalWin += WinNumSUM
            os.system("cls")
            continue
    elif GameNum == '2':
        EvenOddGame(DiceFaceNum, DiceNum)
        if Result == "Change":
            OETotalWin += WinNumOE
            os.system("cls")
            continue
        elif Result == "No":
            OETotalWin += WinNumOE
            os.system("cls")
            continue
    elif GameNum == '3':
        DiceDual(DiceFaceNum, DiceNum)
        if Result == "Change":
            DDTotalWin += WinNumDD
            os.system("cls")
            continue
        elif Result == "No":
            DDTotalWin += WinNumDD
            os.system("cls")
            continue
    elif GameNum == '4' or GameNum == "exit" or GameNum == "Exit":
        os.system("cls")
        print("User Won SUM GAME %s time(s), EVENNESS GAME %s time(s), DICEDUAL GAME %s time(s)"
              %(SumTotalWin, OETotalWin, DDTotalWin))
        print("Program END")
        break
    else:
        print("INVALID PROGRAM...")
        print("...\n...\n...PROGRAM SHUTDOWN")
        break
