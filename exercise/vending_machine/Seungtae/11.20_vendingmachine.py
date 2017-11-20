def Stock():
    f = open("stock.txt", 'r', encoding='utf-8')
    stock = f.readlines()
    for i in range(0, len(stock)):
        stock[i] = stock[i].split()
    print(stock)
    f.close()
    return stock


def Check(kind, price, amount):
    stok = []
    for i in range(0, len(kind)):
        sadd = kind[i] + " " + str(price[i]) + " " + str(amount[i])
        stok.append(sadd)
    return stok


def Write(stock):
    menu = 1
    f = open("stock.txt", 'w', encoding='utf-8')
    if len(stock) >= 1:
        for i in range(0, (len(stock)) - 1):
            f.write(stock[i])
            f.write("\n")
        f.write(stock[(len(stock) - 1)])
        f.close()
    else:
        menu = 0
    return menu


money = 0
monint = 0
menu = 1
force = 0
while True:
    stock = Stock()
    kind = []
    price = []
    amount = []
    for i in range(0, len(stock)):
        kind.append(stock[i][0])
        price.append(int(stock[i][1]))
        amount.append(int(stock[i][2]))
    if menu == 0:
        money = 3.14159
        force = 1
    else:
        print("")
        for j in range(0, len(stock)):
            print("%d.%s:%d원" % (j + 1, kind[j], price[j]), end=', ')
        print("%d.거스름돈 반환" % (len(stock) + 1))
        print("현재 금액은 %d입니다." % money)
        monint = money
        money = input("돈을 투입하세요.: ")
    if money == "admin" or money == 3.14159:
        print("")
        print("=" * 20)
        print("{0:^15}".format("관리자입니다."))
        print("=" * 20)
        print("")
        for i in range(0, len(stock)):
            print("%d.%s의 양은 %d," % (i + 1, kind[i], amount[i]), end=' ')
        print("%d.새로운 커피 추가" % (len(stock) + 1), end=', ')
        print("%d.커피 삭제" % (len(stock) + 2))
        money = monint
        add = input("\n어떤 커피를 추가하시겠습니까.: ")
        if add == "exit":
            print("나갑니다.\n")
        else:
            add = int(add) - 1
            if add in range(0, len(stock)):
                cofnum = int(input("얼마나 추가하시겠습니까: "))
                amount[add] += cofnum
                stock = Check(kind, price, amount)
                Write(stock)
            elif add == len(stock) or force == 1:
                kadd = input("추가할 커피의 이름은?: ")
                kind.append(kadd)
                padd = int(input("그 커피의 가격은?: "))
                price.append(padd)
                aadd = int(input("그 커피의 양은?: "))
                amount.append(aadd)
                stock = Check(kind, price, amount)
                Write(stock)
                force = 0
                menu = 1
            elif add == (len(stock) + 1):
                rmv = int(input("제거할 커피의 번호를 누르세요.: "))
                del kind[rmv - 1]
                del amount[rmv - 1]
                del price[rmv - 1]
                stock = Check(kind, price, amount)
                menu = Write(stock)
            else:
                print("그런 커피는 없습니다.\n")
    else:
        money = int(money)
        money = monint + money
        num = int(input("무엇을 드시려고: ")) - 1
        if num in range(0, len(stock)):
            if money >= price[num] and amount[num] > 0:
                print("%s가 나오는 중입니다.\n" % kind[num])
                money -= price[num]
                amount[num] -= 1
                stock = Check(kind, price, amount)
                Write(stock)
                num = 0
            elif money < price[num]:
                print("돈이 부족합니다.\n")
            else:
                print("품절입니다.\n")
        elif num == len(stock):
            print("거스름돈은 %d입니다." % money)
            break
        else:
            print("메뉴에 없는 주문입니다.\n")