def read_stock():
    coffee_stock = open("coffee_stock.txt", 'r', encoding="utf-8")
    coffee_list = []
    while True:
        line = coffee_stock.readline()
        if not line:
            break
        coffee_list.append(line.strip().split())
    coffee_stock.close()
    return coffee_list


def write_stock(coffee_list):
    coffee_stock = open("coffee_stock.txt", 'w', encoding="utf-8")
    for line_data in coffee_list:
        for data in line_data:
            coffee_stock.write("%s " % data)
        coffee_stock.write("\n")
    coffee_stock.close()


def add_admin_goods_num():
    while True:
        goods_number = input("추가할 개수를 입력하세요: ")
        if goods_number < 0:
            continue


def admin_mode():
    while True:
        add_coffee = 0
        while add_coffee in coffee_dict:
            for i in range(1, len(coffee_list)):
                print("%s. %s: %s개" % (coffee_list[i][0], coffee_list[i][1], coffee_list[i][3]))
            add_coffee = int(input("추가할 커피를 선택하세요.(exit는 종료): "))
        if add_coffee == "exit":
            return
        add_admin_goods_num()


# 프로그램의 시작, 초기화
coffee_list = read_stock()

# exception처리를 아직 배우지 않았기 때문에 dictionary에서 오류날 부분인 맨 처음 줄을 넣고 삭제한다.
coffee_temp = coffee_list[0]
del coffee_list[0]

# 사전 사용해보기
coffee_dict = {}
coffee_value = {}
for line in coffee_list:
    coffee_dict[int(line[0])] = line[1]
    coffee_value[line[1]] = line[2]
coffee_list.insert(0, coffee_temp)

while True:
    money = input("돈을 넣으세요: ")
    if money == "admin":
        admin_mode()
    else:
        break

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
