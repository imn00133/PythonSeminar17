num = int(input("How long?\n"))
SeedOne = int(input("SeedOne: "))
SeedTwo = int(input("SeedTwo: "))
LineLen = int(input("Line length: "))
Number = []
for i in range(1,num+1):
    Number = list(str(i))
    repeat = 0
    NumberInCode = []
    for j in Number:
        if int(j) == 0:
            pass
        else:
            if int(j)%SeedOne == 0 and int(j)%SeedTwo == 0:
                NumberInCode.append("뽁짝")
            elif int(j)%SeedOne == 0 and int(j)%SeedTwo !=0:
                NumberInCode.append("뽁")
            elif int(j)%SeedOne != 0 and int(j)%SeedTwo ==0:
                NumberInCode.append("짝")
    if len(NumberInCode) == 0:
        print(i, end = " ")
    else:
        for j in range(0, len(NumberInCode)):
            if j == len(NumberInCode)-1:
                print(NumberInCode[j], end=" ")
            else:
                print(NumberInCode[j], end="")
    if int(i) % LineLen == 0:
            print("")

