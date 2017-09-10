import copy

def CoffeeOut (CoffeeNum, MoneyLeft, StockList):
    if MoneyLeft < BeverageMenu[CoffeeNum][1]:
        return "Nope"
    elif BeverageMenu[CoffeeNum][2] == 0:
        return "Again"
    else:
        TextCut = list(BeverageMenu[CoffeeNum][0])
        print("\nTakeout %s (Ready)\n" %("".join(TextCut[3:])))
        MoneyLeft = int(MoneyLeft) - BeverageMenu[CoffeeNum][1]
        return MoneyLeft

def MenuOut(Admin):
    StockList = [BeverageMenu[1][2], BeverageMenu[2][2], BeverageMenu[3][2]]
    while 1:
        if Admin == 0:
            print("")
            for i in range(1, 4):
                print(BeverageMenu[i][0], end=" (")
                print(StockList[i-1], end=")")
                print("")
            print("4. Change\n")
            break
        else:
            print("\nCoffee Editor Mode ON...\n")
            for i in range(1,4):
                print(BeverageMenu[i][0], end=" : ")
                print(StockList[i-1])
            print("")
            EditChoice = input("Coffee Change(1~3, exit): ")
            if EditChoice == "exit" or EditChoice == "Exit" or EditChoice == "EXIT":
                return StockList
            else:
                TextCut = list(BeverageMenu[int(EditChoice)][0])
                print("\nProduct %s Check... Stock left: %s\n" %("".join(TextCut[3:]),BeverageMenu[int(EditChoice)][2]))
                StockChange = int(input("Stock Change : "))
                StockList[int(EditChoice)-1] = StockChange
                continue


def AdminMode (OnOff):
    if OnOff == "off":
        pass
    else:
        return(MenuOut("Admin"))

def File(work, CoffeeStock):
    if work == 'read':
        f = open("Coffee_Manage_file.txt", 'r')
        ReturnData = []
        while 1:
            line = list(f.readline())
            if not line:
                break
            if line[-1] == '\n':
                line.pop(-1)
            for i in range(0, len(line)):
                if line[i] == ' ':
                    break
                else:
                    i += 1
            ReturnData.append(int("".join(line[i+1:])))
        f.close()
        return ReturnData
    elif work == 'write':
        ManageData = {1:["Black_Coffee",CoffeeStock[0]], 2:["Milk_Coffee",CoffeeStock[1]], 3:["Gooooood_Coffee",CoffeeStock[2]]}
        f = open("Coffee_Manage_file.txt", 'w')
        for i in ManageData:
            f.write("%s %s\n" %(ManageData[i][0], ManageData[i][1]))
        f.close()

def StockSync(NewStock):
    for i in range(0, 3):
        BeverageMenu[i + 1][2] = NewStock[i]

StockHandOver = copy.deepcopy(File('read',File('read',[0,0,0])))
print(StockHandOver)
BeverageMenu = {1:["1. Black Coffee",100, StockHandOver[0]], 2: ["2. Milk Coffee", 150, StockHandOver[1]],
                3:["3. Gooooood Coffee", 250, StockHandOver[2]], 4:["Change",""], "admin":AdminMode("off")}
print(BeverageMenu)
UserMoney = int(input("Money : "))
Processing = 0
UserChoice = 0
while 1:
    if UserMoney < 100:
        break
    MenuOut(0)
    UserChoice = input("Choose Coffee : ")
    if UserChoice == "admin":
        StockHandOver = AdminMode("on")
        StockSync(StockHandOver)
        continue
    if int(UserChoice) < 1 and int(UserChoice) > 4:
        continue
    elif int(UserChoice) == 4:
        break
    else:
        Processing = CoffeeOut(int(UserChoice), UserMoney, StockHandOver)
        if Processing == "Nope":
            break
        elif Processing == "Again":
            print("Sold Out")
            continue
        else:
            StockHandOver[int(UserChoice) - 1] = StockHandOver[int(UserChoice)-1] - 1
            StockSync(StockHandOver)
            UserMoney = Processing
            print("Money Left : %s\n" %(UserMoney))
            continue
if int(UserChoice) == 4:
    print("\nChange : %s" %UserMoney)
    File('write', StockHandOver)
if Processing == "Nope" or UserMoney < 100:
    print("\nNot Enough Money... Change : %s" %UserMoney)
    File('write', StockHandOver)