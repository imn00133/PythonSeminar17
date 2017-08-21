import time
import os

def NotEnoughMoney(Money):
    print("Not enough Money")
    for i in range(0,3):
        time.sleep(0.5)
        print(".")
    time.sleep(0.5)
    print("Automatic Change System")
    for i in range(0,3):
        time.sleep(0.5)
        print(".")
    time.sleep(0.5)
    print("...Change: %d Won" % Money)

def CoffeeOut(Coffee):
    print("\nHeating water")
    for i in range(0,3):
        time.sleep(0.5)
        print(".")
    time.sleep(0.5)
    print("Dripping Coffee")
    for i in range(0,3):
        time.sleep(0.5)
        print(".")
    time.sleep(0.5)
    print("%s Ready, Please take the coffee\n" %Coffee)
    time.sleep(1)
    os.system("cls")

os.system("cls")
UserMoney = int(input("Please insert money: "))
while 1:
    time.sleep(0.5)
    if UserMoney <100:
            NotEnoughMoney(UserMoney)
            break
    print("")
    print('''1. Black Coffee(100\\)
2. Milk Coffee (150\\)
3. Gooooooooooood Coffee (250\\)
4. Change
    '''
          )
    UserChoice = input("Choose: ")
    if UserChoice == '1':
        if UserMoney < 100:
            NotEnoughMoney(UserMoney)
            break
        else:
            CoffeeOut('Black Coffee')
            print("%d Won left\n" %(UserMoney-100))
            UserMoney = UserMoney - 100
            continue
    elif UserChoice == '2':
        if UserMoney < 150:
            NotEnoughMoney(UserMoney)
            break
        else:
            CoffeeOut("Milk Coffee")
            print("%d Won left\n" %(UserMoney-150))
            UserMoney = UserMoney - 150
            continue
    elif UserChoice == '3':
        if UserMoney < 250:
            NotEnoughMoney(UserMoney)
            break
        else:
            CoffeeOut("Gooooooooooood Coffee")
            print("%d Won left\n" %(UserMoney-250))
            UserMoney = UserMoney - 250
            continue
    elif UserChoice == '4':
        print("Change: %d Won" %UserMoney)
        break
    else:
        continue

