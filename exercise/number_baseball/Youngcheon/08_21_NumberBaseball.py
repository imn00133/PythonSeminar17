import random
fail = 0                                                                    # 입력 체크용 변수
while 1:                                                                    # 재시작용 무한루프
    NumberLen = int(input("Number of Number: "))
    hit = 0                                                                 # 시도횟수 초기화
    AnsList = []
    AnsListLen = 0
    while 1:
        a = random.randint(0,9)
        AnsList.append(a)
        if int(len(set(AnsList))) == int(AnsListLen):
            del AnsList[AnsListLen]
        else:
            AnsListLen = AnsListLen + 1
        if len(set(AnsList)) == NumberLen:
            break
    print(AnsList)                                                         # 정답을 알아야 테스트를 하니 남겨둔 줄
    while 1:                                                                # 입력받는 무한루프
        hit = hit + 1                                                       # 입력 횟수 변수
        Sco = [0, 0, 0]                                                     # 순서대로 B, S, O 개수 초기화
        if fail == 0:
            a = input()
        else:
            a = input("입력이 잘못되었습니다.\n")
        ut = 1
        Max = 1
        for i in range(0, NumberLen):
            Max = Max * 10
        if int(a) < 0:                                                      # 중도포기과정(1/3)
            ut = 0
            print("포기하셨습니다")
            break                                                           # 입력받는 무한루프 탈출
        elif int(a) <= int(int(Max)/10) or int(a) > Max:
            fail = 1
            continue                                                        # 다시 입력받는 무한루프 처음부터
        else:
            fail = 0                                                        # 여기까지가 입력을 받는 코드
        for i in range(0, NumberLen):
            for j in range(0, NumberLen):                                            # '4번 돌리겠다'가 겹으로 총 16번(4*4)
                if i == j:
                    if int(AnsList[i]) == int(a[j]):                           # 두 숫자가 같으면(즉 숫자와 위치가 모두 같으면)
                        Sco[1] = Sco[1] + 1                                 # 쓰뚜라이크
                else:
                    if int(AnsList[i]) == int(a[j]):                           # 자리수는 다른데 숫자가 같은경우
                        Sco[0] = Sco[0] + 1                                 # 볼
        Sco[2] = NumberLen-Sco[0]-Sco[1]                                   # 16회 비교 후 B도 S도 없으면 아웃
        print("B : %d  S : %d  O : %d" % (Sco[0], Sco[1], Sco[2]))          # 점수판
        if Sco[1] == NumberLen:                                                     # 스트라이크가 4개 = 다맞춤
            print("축하합니다\n%d번만큼 질문하여 맞추셨습니다" % hit)
            break                                                           # 입력받는 무한루프 탈출
    if ut == 0:                                                             # 중도포기과정(2/3)
        break                                                               # 재시작 무한루프 탈출
    else:                                                                   # 중도포기를 안했으면 재시작 무한루프내에서 선택
        while 1:                                                            # 재시작 문구 출력용 무한루프
            ret = input("다시하시겠습니까?(yes/no)\n")
            if ret != "yes" and ret != "no":
                continue
            else:
                break                                                       # 잘 입력받으면 무한루프 탈출
        if ret == "yes":
            continue                                                        # 다시 시작 --> 전체 재시작 무한루프 반복
        else:
            print("종료합니다")
            break                                                           # 종료 --> 전체 재시작 무한루프 탈출

# 입력은 4자리받음
# 네자리는 모두 다른 숫자
# 네자리가 아닌 다른 자릿수 입력은 "입력이 잘못되었습니다" 후 재입력
# 음수 입력은 "포기하셨습니다" 후 종료
# 맞춘경우 '''축하합니다 \n x번 만큼 질문하여 맞추셨습니다'''출력
# 이어서 "다시하시겠습니까?(yes/no)" 출력
# yes는 재시작 no는 "종료합니다"출력 후 종료 다른 문자열은 출력했던 문구 재출력

