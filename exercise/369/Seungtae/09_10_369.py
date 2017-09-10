def First(number):
    return number % 10


print("우리의 삼육구 게임이 어디까지 갈까?")
n = int(input())
i = 1
while i <= n:
    a = First(i)
    if a == 0:
        print("%d" % i, end=" ")
    elif a % 3 == 0:
        print("짝", end=" ")
    else:
        print("%d" % i, end=" ")
    i += 1
