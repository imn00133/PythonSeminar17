import random

user_door_num = int(input("문의 개수를 입력하세요: "))
exec_num = int(input("실행횟수를 입력하세요: "))
open_door = int(input("사회자가 열어줄 문의 개수를 입력하세요: "))
first_door_win = 0
change_door_win = 0

# 문에 당첨제비 넣기
# 사실 확률만 계산할꺼면 맨 앞에다가 car를 넣어주면 고려할 점이 적어지지만, 실제 게임을 코딩할 땐, 사람이 뽑으니..
for exec_times in range(0, exec_num):
    door = []
    for i in range(0, user_door_num):
        door.append("goat")
    door[random.randrange(0, len(door))] = "car"

    # 하나 뽑았을 때 당첨되었으면 first 선택에서 이김, 그 후 바꾼 것 테스트
    choose_door = random.randrange(0, len(door))
    # 뽑았을 경우 다음에 문을 열어보는 건 필요하지 않아 넘긴다.
    if door[choose_door] == "car":
        first_door_win += 1
        continue
    door.pop(choose_door)

    # 사회자가 뽑아서 보여줌
    for i in range(open_door):
        choose_door = random.randrange(0, len(door))
        while door[choose_door] == "car":
            choose_door = random.randrange(0, len(door))
        door.pop(choose_door)

    # 바꿔서 확인
    choose_door = random.randrange(0, len(door))
    if door[choose_door] == "car":
        change_door_win += 1

    # 하도 오래결려서 몇 퍼센트인지 출력
    if exec_times % 1000 == 0:
        print("%0.2f%%" % (exec_times/exec_num*100))

print("바꾸지 않았을 때 이긴 횟수: %d" % first_door_win)
print("바꾸지 않았을 때 이길 확률: %0.2f%%" % (first_door_win/exec_num*100))
print("바꾸지 않았을 때 이론적으로 이길 확률: %0.2f%%" % (1/user_door_num*100))
print("바꾸었을 때 이긴 횟수: %d" % change_door_win)
print("바꾸었을 때 이길 확률: %0.2f%%" % (change_door_win/exec_num*100))
print("바꾸었을 때 이론적으로 이길 확률: %0.2f%%" % ((user_door_num-1)/(user_door_num*(user_door_num-open_door-1))*100))
