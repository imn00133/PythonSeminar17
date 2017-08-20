import random
trial=0
doorcount=int(input("Coose the Number of Doors \n"))
while trial<=100000:
    win=0
    if doorcount>1:
        Choice=random.randint(1,doorcount+1)
        Answer=random.randint(1,doorcount+1)
        if Choice==Answer:
            print("Success")
            trial+=1
            win+=1
        else:
            print("Fail")
            trial+=1
    else:
        print("2 이상의 숫자를 입력하십시오")
        break
    print(win/trial)
    print("%d번째 시도" %trial)


# 바꾸지 않을 경우를 가정함
# 따라서 Choice도 랜덤, Answer도 랜덤일 때 choice=random 이면 success
# 문제는 한번 끝나고 doorcount를 설정하는 곳으로 되돌아감