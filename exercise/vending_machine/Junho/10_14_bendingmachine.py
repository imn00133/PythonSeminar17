account=str(input("당신은 뭐시여"))
if account=="admin":
    f=open("Coffee Stock.txt", "r", encoding="utf-8")
    menu_status = []
    while True:
        menu = f.readline()
        if not menu: break
        menu_status.append(menu.split())
    f.close()
    dict_menu_status={}
    for adder in menu_status:
        dict_menu_status[adder[1]]=int(adder[0])
    print(dict_menu_status)
    print("사용자 메뉴 1. 재고변경 2. 가격변경")
    admin_choice=int(input("뭐할라고"))
    if admin_choice==1:
        while True:
            change_stock=input("무슨 커피를 더 넣으시겠습니까?")
            if change_stock in dict_menu_status.keys():
                adding_stock = int(input("몇 개 추가할래?"))
                menu_status[dict_menu_status[change_stock]-1][3] = str(int(menu_status[dict_menu_status[change_stock]-1][3]) + adding_stock)
                break
            else:
                continue
    if admin_choice==2:
        while True:
            change_value=input("무슨 커피의 가격을 바꾸시겠습니까?")
            if change_value in dict_menu_status.keys():
                changing_value = int(input("얼마로 바꿀래?"))
                menu_status[dict_menu_status[change_value]-1][2] = str(int(changing_value))
                break
            else:
                continue
    print(menu_status)
    with open("Coffee Stock.txt", "w", encoding="utf-8") as f:
        for index_menu_status in menu_status:
            for j in index_menu_status:
                f.write(j + " " )
            f.write("\n")
else:
    money=int(input("돈을 입력하십시오. \n"))
    while True:
        choice=int(input("1. 블랙커피(100원), 2. 밀크커피(150원), 3. 고급커피(250원), 4. 거스름돈 \n"))
        price=[100,150,250,0]
        pick=price[choice-1]
        change=money-pick
        if money>=pick and pick>0:
            print(change)
            print("원 남았습니다.")
            money = change
        elif money<pick:
            print(" 거슬러줄게 돈 벌어와 ")
            break
        elif pick==0:
            print(" %d 거슬러 드리겠습니다. ㅅㄱ " %change)
            break