#admin에서 메뉴 입력과 삭제, 재고 입력과 삭제, 가격조정 가능

number_of_coffee=3
coffee={1:'블랙커피', 2:'밀크커피', 3:'고급커피'}
stock={1 : 10, 2 : 10, 3 : 10}
cost={1:100, 2:150, 3:250}

while True:
    money = input("자판기에 돈을 넣으세요 : ")
    if money == "admin":
        while True:
            print("관리자 모드입니다.")
            for i in range(1,number_of_coffee+1):
                print(str(i)+"."+coffee[i]+" : "+str(stock[i])+"개")
            add = input("기존 커피의 재고를 추가하려면 'stock_add'를, \n"
                        "기존 커피의 재고를 제거하려면 'stock_remove'를, \n"
                        "새로운 커피를 추가하려면 'type_add'를, \n"
                        "기존 커피를 제거하려면 'type_remove'를, \n"
                        "기존 커피의 가격을 조정하려면 'cost_renewal'을 입력하세요.(exit를 입력하면 종료됩니다.) : ")
            if add == "type_add":
                name_of_new_coffee = input("새로운 커피의 이름을 입력하세요 : ")
                stock_of_new_coffee = int(input("추가할 새로운 커피의 개수를 입력하세요 : "))
                cost_of_new_coffee = int(input("추가할 새로운 커피의 가격을 입력하세요 : "))
                coffee[number_of_coffee+1]= name_of_new_coffee
                stock[number_of_coffee+1]=stock_of_new_coffee
                cost[number_of_coffee+1]= cost_of_new_coffee
                number_of_coffee = number_of_coffee + 1
            elif add == "type_remove":
                coffee_to_remove = int(input("제거할 커피를 선택하세요 : "))
                if coffee_to_remove not in range(1,number_of_coffee+1):
                    print("그런건 원래 없었습니다.")
                else:
                    coffee_list =[]
                    stock_list =[]
                    cost_list =[]
                    for i in range(1,number_of_coffee+1):
                        coffee_list.append(coffee[i])
                        stock_list.append(stock[i])
                        cost_list.append(cost[i])
                    del coffee_list[coffee_to_remove-1]
                    del stock_list[coffee_to_remove-1]
                    del cost_list[coffee_to_remove-1]
                    number_of_coffee = number_of_coffee - 1
                    coffee={}
                    stock={}
                    cost={}
                    for i in range(1,number_of_coffee+1):
                        coffee[i]=coffee_list[i-1]
                        stock[i]=stock_list[i-1]
                        cost[i]=cost_list[i-1]
            elif add == "stock_add":
                type_to_add = int(input("추가할 커피를 선택하세요 : "))
                stock_to_add = int(input("추가할 개수를 입력하세요 : "))
                if type_to_add > number_of_coffee or type_to_add <= 0:
                    print("그런건 없습니다.")
                else:
                    stock[type_to_add] = stock[type_to_add] + stock_to_add
            elif add == "stock_remove":
                type_to_remove = int(input("재고를 제거할 커피를 선택하세요 : "))
                stock_to_remove = int(input("제거할 개수를 입력하세요 : "))
                if type_to_remove not in range(1,number_of_coffee+1):
                    print("그런건 없습니다.")
                elif type_to_remove in range(1,number_of_coffee+1):
                    if stock[type_to_remove] < stock_to_remove:
                        stock[type_to_remove] = 0
                    else:
                        stock[type_to_remove] = stock[type_to_remove] - stock_to_remove
            elif add == "cost_renewal":
                type_to_renew_cost=int(input("가격을 재설정할 커피를 선택하세요 : "))
                if type_to_renew_cost not in range(1,number_of_coffee+1):
                    print("그런건 없습니다.")
                else:
                    new_cost = int(input("새로운 가격을 입력하세요 : "))
                    cost[type_to_renew_cost]=new_cost
            elif add == "exit":
                print("관리자 모드를 끝냅니다.")
                break
            else:
                print("그런건 없습니다.")
    else:
        while True:
            money = int(money)
            for i in range(1,number_of_coffee+1):
                print("%d%s%s" %(i,'. ',coffee[i]))
            print("%d%s" %(number_of_coffee+1,'. 거스름돈'))
            choice=int(input('선택하세요 : '))
            if choice not in range(1,number_of_coffee+2):
                print("그런건 없습니다.")
            elif choice != number_of_coffee+1 and money < cost[choice]:
                print("돈이 부족합니다."+"\n거스름돈 : "+str(money)+"원")
                break
            elif choice == number_of_coffee+1:
                print("거스름돈 : "+str(money)+"원")
            elif stock[choice] == 0:
                print("품절입니다.")
            else:
                print(coffee[choice]+"(이)가 나왔습니다.")
                stock[choice] = stock[choice]-1
                money = money - cost[choice]
                print(money)
