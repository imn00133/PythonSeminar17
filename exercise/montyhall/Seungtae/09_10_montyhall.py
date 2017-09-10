import random

num = 1
change = 0
Door = [1, 0, 0]
trial = int(input("시행수를 입력하세요: "))

while num <= trial:
    print("Loading... %s%%" % (num * 100 / trial))
    choice = random.randint(0, 2)
    if Door[choice] == 1:
        pass
    else:
        change += 1
    num += 1

print("바꾸었을 때 확률은 %s%%이다." % (change * 100 / trial))
