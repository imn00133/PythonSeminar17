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