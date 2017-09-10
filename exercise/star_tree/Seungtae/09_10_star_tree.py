i = 1
print("그리고 싶은 별 트리의 줄 수를 입력하세요: ")
n = int(input())

while True:
    if n <= 0:
        print("종료합니다.")
        break
    elif n >= 80:
        print("1~79까지 입력할 수 있습니다.")

    else:
        while i <= n:
            print(" " * (n - i) + "*" * (2 * i - 1))
            i += 1
            break
