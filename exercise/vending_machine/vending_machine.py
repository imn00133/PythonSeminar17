def read_stock():
    """
    txt파일을 읽어 coffee_list를 반환해준다.
    :return: coffee_list는 커피번호, 제품명, 가격, 제고로 이뤄진 2차원 배열이다.
             error는 오류가 있을 경우 오류메세지와 함께 반환되는 값이다.
    """
    try:
        error = ""
        coffee_stock = open("coffee_stock.txt", 'r', encoding="utf-8")
    except FileNotFoundError as error:
        write_stock([])
        coffee_stock = open("coffee_stock.txt", 'r', encoding="utf-8")
        print("파일이 없습니다.")
    coffee_list = []
    while True:
        line = coffee_stock.readline()
        if not line:
            break
        coffee_list.append(line.strip().split())
    coffee_stock.close()
    return coffee_list, error


def write_stock(coffee_list):
    """
    파일에 coffee_list를 쓴다.
    :param coffee_list를 받는다.
    """
    # coffee_list가 비어있을 경우, 초기화를 사용한다.
    if not coffee_list:
        coffee_list = [["번호", "제품명", "가격", "재고"]]
    coffee_stock = open("coffee_stock.txt", 'w', encoding="utf-8")
    for line_data in coffee_list:
        for data in line_data:
            coffee_stock.write("%s " % data)
        coffee_stock.write("\n")
    coffee_stock.close()


def add_admin_goods_num(add_coffee):
    """
    물품의 개수를 변경한다.
    :param add_coffee: 변경한 커피의 번호
    """
    goods_number = -1
    while goods_number < 0:
        goods_number = int(input("추가할 개수를 입력하세요: "))
    coffee_list[add_coffee][len(coffee_list[0])-1] = str(int(coffee_list[add_coffee][len(coffee_list[0])-1]) + goods_number)


def add_admin_goods():
    """
    물품을 추가한다.
    """
    goods_name = input("추가할 물품을 입력하세요.: ")
    goods_value = input("물품의 가격을 입력하세요.: ")
    goods_number = input("물품의 개수를 입력하세요.: ")
    coffee_list.append([str(len(coffee_list)), goods_name, goods_value, goods_number])


def del_admin_goods():
    pass


def admin_mode():
    coffee_num = 0
    while coffee_num != "exit":
        for i in range(1, len(coffee_list)):
            print("%s. %s: %s개" % (coffee_list[i][0], coffee_list[i][1], coffee_list[i][3]))
        print("="*30)
        choice = int(input("1. 물품의 개수를 추가\n2. 물품을 추가\n3. 물품을 삭제\n4. 종료\n선택해주세요.: "))
        while choice <= 0 or choice > 4:
            choice = int(input("1. 물품의 개수를 추가\n2. 물품을 추가\n3. 물품을 삭제\n4를 입력하면 종료됩니다.: "))
        if choice == 1:
            while not(coffee_num in coffee_dict):
                for i in range(1, len(coffee_list)):
                    print("%s. %s: %s개" % (coffee_list[i][0], coffee_list[i][1], coffee_list[i][3]))
                coffee_num = int(input("추가할 커피를 선택하세요.(exit는 종료): "))
            add_admin_goods_num(coffee_num)
            coffee_num = 0
            write_stock(coffee_list)
        elif choice == 2:
            for i in range(1, len(coffee_list)):
                print("%s. %s: %s개" % (coffee_list[i][0], coffee_list[i][1], coffee_list[i][3]))
            add_admin_goods()
            write_stock(coffee_list)
        elif choice ==3:
            while not(coffee_num in coffee_dict):
                for i in range(1, len(coffee_list)):
                    print("%s. %s: %s개" % (coffee_list[i][0], coffee_list[i][1], coffee_list[i][3]))
                coffee_num = int(input("추가할 커피를 선택하세요.(exit는 종료): "))
            add_admin_goods_num(coffee_num)
            coffee_num = 0
            del_admin_goods()
            write_stock(coffee_list)
        elif choice == 4:
            return


# 프로그램의 시작, 초기화
coffee_list, file_error = read_stock()

# 첫번째 행의 오류 무시
# coffee_dict: key=coffee_num, value=coffee_name
# coffee_value: key=coffee_name, value=coffee_value
coffee_dict = {}
coffee_value = {}
for line in coffee_list:
    try:
        coffee_dict[int(line[0])] = line[1]
        coffee_value[line[1]] = int(line[2])
    except:
        pass

if file_error != "":
    print("재고가 초기화되어 admin에 접속합니다.")
    admin_mode()

while True:
    money = input("돈을 넣으세요: ")
    if money == "admin":
        admin_mode()
    else:
        money = int(money)
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
    if user_choice == len(coffee_dict):
        break
    money -= coffee_value[coffee_dict[user_choice]]
    print("%d원이 남았습니다." % money)
print("거스름돈 %d원을 돌려주었습니다." % money)
