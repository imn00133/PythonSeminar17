row = int(input("몇 행? : "))
column = int(input("몇 열? : "))
for k in range(0, row):
    for i in range(1, column+1):
        print((i-1)*row+1 +k, end = " ")
    print()