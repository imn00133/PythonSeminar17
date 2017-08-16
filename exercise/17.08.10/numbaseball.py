import random

while True:
    #컴퓨터의 숫자를 만들어줄 temp list생성
    temp=[i for i in range(0,10)]

    #랜덤으로 숫자를 4개 뽑음
    com_num = []
    while len(temp)>6:
        com_num.append(temp.pop(random.randint(0,len(temp)-1)))
    print(com_num)

    # 프로그램의 시작
    prg_cnt=0
    while True:
        # 사용자에게서 숫자를 받음, 문자열을 문자의 리스트로 변경
        user_input=list(input("네 자리 중복되지 않는 숫자를 입력해주세요: "))
        if user_input[0]=='-':
            print("포기하셨습니다.")
            # while을 빠져나가기 위한 종료 플래그 입력
            flag="no"
            break
        elif len(user_input)!=4:
            print("네 자리를 입력해주세요.")
            continue
        elif len(set(user_input))!=4:
            print("중복되지 않도록 입력해주세요.")
            continue

        # 문자를 숫자로 변경
        user_input=[int(i) for i in user_input]
        prg_cnt+=1

        # 스트라이크와 볼 확인
        strike_num, ball_num=0, 0
        for i in range(0,4):
            for j in range(0,4):
                if com_num[i]==user_input[j] and i==j:
                    strike_num+=1
                elif com_num[i]==user_input[j]:
                    ball_num+=1

        # 스트라이크와 볼, 아웃 출력
        if strike_num!=4:
            print("%sS %sB %sO 입니다." %(strike_num, ball_num, 4-strike_num-ball_num))

        # 종료계산
        else:
            print("축하합니다.\n%s번 만큼 질문하여 맞추셨습니다." %prg_cnt)
            while True:
                flag=input("다시하시겠습니까? (yes/no): ")
                if flag=="yes" or flag=="YES" or flag=="NO" or flag=="no":
                    prg_cnt=0
                    break
        if flag=="YES" or flag=="yes" or flag=="NO" or flag=="no":
            break
    if flag=="NO" or flag=="no":
        break

print("종료합니다.")