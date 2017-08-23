user_number = int(input("횟수를 입력하시요: "))
for num in range(1, user_number+1):
    # 계산하기 위한 temp와 짝 소리 변수
    num_temp = num
    palm_times = ""
    # 각 자리 수에 3, 6, 9가 들어가는지 확인
    while num_temp != 0:
        remainder = num_temp % 10
        num_temp //= 10
        if remainder != 0 and remainder % 3 == 0:
            palm_times += "짝"
        if remainder != 0 and remainder % 2 == 0:
            palm_times += "뽁"

    if palm_times == "":
        print(num, end=" ")
    # 문자열을 뒤집는 방법 [::-1]이라고 한다. slice를 -1단계씩 하는 것.
    else:
        print(palm_times[::-1], end=" ")
    if num % 20 == 0:
        print("")
