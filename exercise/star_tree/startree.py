while True:
    user_num=int(input("그리고 싶은 별 트리의 줄 수를 입력하세요: "))
    if user_num==0 or user_num>=80:
        print("1~79까지 입력할 수 있습니다.")
        continue
    if user_num<0:
        print("종료합니다.")
        break

    line = 0
    while line != user_num:
        print(" "*(user_num-line-1)+"*"*(2*line+1))
        line += 1