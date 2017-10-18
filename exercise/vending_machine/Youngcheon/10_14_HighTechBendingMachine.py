import os

def MenuOut(AdminCode):
    File('read')
    if AdminCode == 0:
        for i in range(len(MenuListNum)):
            print("%d. %s (%d)" %(MenuListNum[i], MenuList[i][0], MenuList[i][1]))
        print("%d. Change (Exit)\n" %(len(MenuListNum)+1))
    else:
        for i in range(len(MenuListNum)):
            print("Stock #%-3d ID: %-15s  Price: %5d  Stock left: %4d"
                  %(MenuListNum[i], MenuList[i][0], MenuList[i][1], MenuList[i][2]))
        print("")

def MenuChange():
    while 1:
        Mode = input("Menu Manage Mode... \n\nMenu/Stock : ")
        if Mode == 'Menu':
            ChangeWay = input("Add/Del? : ")
            if ChangeWay == "Add":
                NewMenuID = input("\nNew Menu: ")
                NewMenuPrice = int(input("New Menu Price : "))
                NewMenuStock = int(input("New Menu Stock: "))
                NewMenu = [NewMenuID, NewMenuPrice, NewMenuStock]
                MenuList.append(NewMenu)
                MenuListNum.append(len(MenuListNum)+1)
            elif ChangeWay == 'Del':
                Choice = input("ID or #? : ")
                if Choice == 'ID':
                    DelMenuID = input("Deleted Menu ID: ")
                    MenuListNum.remove(len(MenuListNum))
                    for i in range(0, len(MenuList)-1):
                        if MenuList[i][0] == DelMenuID:
                            MenuList.pop(i)
                elif Choice == "#":
                    DelMenuNum = int(input("Deleted Menu Number : "))
                    MenuListNum.remove(len(MenuListNum))
                    MenuList.pop(DelMenuNum-1)
        elif Mode == 'Stock':
            Choice = input("ID or #? : ")
            Hold = 0
            if Choice == "ID":
                StockChangeID = input("Changed Menu ID : ")
                for i in range(0, len(MenuList)):
                    if MenuList[i][0] == StockChangeID:
                        Hold = int(i)
                        break
            elif Choice == "#":
                StockChangeNum = int(input("Changed Menu Number : "))
                Hold = StockChangeNum - 1
            StockPrice = input("Stock/Price? : ")
            if StockPrice == 'Stock':
                StockChange = int(input("Changed Stock : "))
                MenuList[Hold][2] = MenuList[Hold][2] + StockChange
            elif StockPrice == 'Price':
                PriceChange = int(input("Changed Price : "))
                MenuList[Hold][1] = PriceChange
        os.system('cls')
        MenuOut(1)
        UserChoice = input("Anymore Changes?(y/n) : ")
        if UserChoice == "y":
            continue
        else:
            File('write',MenuList, MenuListNum)
            os.system('cls')
            return

def File(do, MenuList = [], MenuListNum = []):
    if do == 'write':
        f = open("Menu_Stock.txt", 'w', encoding='utf-8')
        for i in range(0, len(MenuListNum)):
            f.write("%d/%s/%d/%d\n" % (MenuListNum[i], MenuList[i][0], MenuList[i][1], MenuList[i][2]))
        f.close()
    elif do == 'read':
        f = open("Menu_Stock.txt", 'r', encoding='utf-8')
        MenuList = []
        MenuListNum = []
        while 1:
            line = f.readline()
            if not line:
                break
            Data = line.strip().split('/')
            MenuListNum.append(int(Data[0]))
            Data.pop(0)
            Data[1] = int(Data[1])
            Data[2] = int(Data[2])
            MenuList.append(Data)
        return (MenuList, MenuListNum)

MenuListNum = []
MenuList = []
(MenuList, MenuListNum) = File('read')
while 1:
    os.system('cls')
    Money = (input("Money please : "))
    if Money == 'admin':
        os.system('cls')
        print("Admin Excess code...\n")
        UserCode = input()
        if UserCode == 'HellYeah':
            os.system('cls')
            print("Admin mode on...\n")
            MenuOut(1)
            MenuChange()
        else:
            continue
    else:
        while 1:
            Money = int(Money)
            os.system('cls')
            print("Money left : %d" %Money)
            MenuOut(0)
            UserChoice = int(input("Coffee # : "))
            if UserChoice == len(MenuListNum)+1:
                print("Change : %d" %Money)
                break
            if Money < MenuList[UserChoice-1][1]:
                print("Not Enough Money....\nChange: %d" %Money)
                break
            MenuList[UserChoice-1][2] = MenuList[UserChoice-1][2] - 1
            Money = Money - MenuList[UserChoice-1][1]
    Try = input("More Menu? (y/n) : ")
    if Try == 'y':
        continue
    else:
        break


