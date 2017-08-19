import random
retry = 1
while retry:                          		#흔한 재입력받기 무한루프
    choice = input("Change? yes / no\n")
    doornum = int(input("Door number?: "))
    runtime = int(input("Repeat count: "))  	#입력받는다
    win = 0 					#for문 안에서 초기화 방지, 1을 선택한 경우의 수
    for j in range(0, runtime):
        if int(j) % 1000 == 0:
            print(int((int(j)/runtime)*1000)/10, end="%\n")
        answer = []
        for i in range(0, doornum):
            i = 0
            answer.append(i)
        one = random.randint(0, doornum-1)
        answer[one] = 1				# 0,1로 이루어진 길이 3짜리 리스트, 단 1(당첨)은 반드시 1개만
        pick = random.randint(0, doornum-1)  		#원래 사람이 골라야하지만 10만번 입력은 싫으니 랜덤뽑기
        if choice == 'no':          		#바꾸지 않는 경우 그냥 배열이랑 값이 1인지 확인
            if answer[pick] == 1:
                win += 1
        else:                  		         #바꾸는 경우
            answer.pop(pick)   		         #첫 선택지는 버림
            for i in range(0, doornum):
                if answer[int(i)] == 0:    	         #남은 선택지들 중 0인 것을 사회자가 공개 (pop으로 제거)
                    answer.pop(int(i))
                    break
            repick = random.randint(0, (doornum-3))
            if answer[repick] == 1:   		#선택(남은 doornum-2개의 선택지들 중 하나)의 결과를 비교
                win += 1
    print("Probability: %s, Runtime: %d" % ((win/runtime), runtime))    #확률 = 특정 사건(1을 뽑은) 경우의 수 / 시행 횟수
    if choice == "yes":
        print("Ideal: %s" %((doornum-1)/(doornum*(doornum-2))))
    else:
        print("Ideal: %s" % (1/doornum))
    reinput = input("Retry? yes / no\n")
    if reinput == 'yes':
        retry = 1
    else:
        retry = 0
print("End program")