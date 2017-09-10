import random
ComChoice1 = random.randint(1,9)    #천의자리
ComChoice2 = random.randint(0,9)    #백의자리
ComChoice3 = random.randint(0,9)    #십의자리
ComChoice4 = random.randint(0,9)    #일의자리
Answer = 1000*ComChoice1+100*ComChoice2+10*ComChoice3+ComChoice4
print(Answer)
print("천의자리 숫자를 정하십시오. 1~9 범위 내 ")
UserChoice1 = int(input())
print("백의자리 숫자를 정하십시오. 0~9 범위 내 ")
UserChoice2 = int(input())
print("십의자리 숫자를 정하십시오. 0~9 범위 내 ")
UserChoice3 = int(input())
print("일의자리 숫자를 정하십시오. 0~9 범위 내 ")
UserChoice4 = int(input())
Request = 1000*ComChoice1+100*ComChoice2+10*ComChoice3+ComChoice4
Ball=0
Strike=0
Out=0
Score=(Ball, Strike, Out)
if ComChoice1==UserChoice1 or ComChoice2==UserChoice2 or ComChoice3==UserChoice3 or ComChoice4==UserChoice4 :
    Strike += 1
elif ComChoice1==UserChoice2 or ComChoice1==UserChoice3 or ComChoice1==UserChoice4 :
    Ball += 1
elif ComChoice2==UserChoice3 or ComChoice2==UserChoice4 :
    Ball += 1
elif ComChoice3==UserChoice4:
    Ball += 1
else:
    Out += 1
print("%d 볼, %d 스트라이크, %d 아웃" %(Ball,Strike,Out))