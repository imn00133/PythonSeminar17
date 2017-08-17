print("아무 숫자나 입력해 보세욤~")
UserChoice=int(input())
for Num in [str(index) for index in range(1, UserChoice+1)]:
    times = Num.count('3') + Num.count('6') + Num.count('9')
    if times:
        print("짝!" * times)
    else:
        print(Num)