print("아무 숫자나 입력해 보세욤~")
UserChoice=int(input())
for Num in [str(index) for index in range(1, UserChoice+1)]:
    times1 = Num.count('3') + Num.count('6') + Num.count('9')
    times2 = Num.count('2') + Num.count('4') + Num.count('6') + Num.count('8')
    if times1 or times2:
        print("뽕!" * times2 + "짝!" * times1)
    else:
        print(Num)