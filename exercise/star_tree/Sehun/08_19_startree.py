while True:
    line = int(input("그리고 싶은 별 트리의 줄 수를 입력하세요: "))
    if line >= 80:
        print("1~79까지 입력할 수 있습니다.")
    elif line >= 1 and line < 80:
        for k in range(1, (line + 1)):
            print(' ' * (line - k), end="")
            print('*' * ((k * 2) - 1))
    elif line <= 0:
        print("종료합니다.")
        break
