money = int(input("돈을 넣으세요: "))
# 사전 사용해보기
coffee_dict = {1: "블랙커피", 2: "밀크커피", 3: "고급커피", 4: "거스름돈"}
coffee_value = {"블랙커피": 100, "밀크커피": 150, "고급커피": 250}

# 100원 이하는 무조건 거스름 돈으로 돌려주면서 끝낸다.
while money > 100:
    # 가격 및 고를 수 있는 커피 출력
    for i in range(1, len(coffee_dict)+1):
        print("%d. %s" % (i, coffee_dict[i]), end=" ")
        if i != len(coffee_dict):
            print("(%d원), " % coffee_value[coffee_dict[i]], end="")
        else:
            print("")

    # 커피를 선택
    user_choice = 0
    while user_choice <= 0 or user_choice > len(coffee_dict):
        user_choice = int(input("마실 커피를 골라주세요: "))
    if user_choice == 4:
        break
    money -= coffee_value[coffee_dict[user_choice]]
    print("%d원이 남았습니다." % money)
print("거스름돈 %d원을 돌려주었습니다." % money)
