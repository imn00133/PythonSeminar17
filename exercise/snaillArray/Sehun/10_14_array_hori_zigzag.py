row = int(input("몇 행? : "))
column = int(input("몇 열? : "))
for r in range(1, row+1):
    if r%2==1:
        for c in range(1, column+1):
            if c == column:
                print(c + column * (r-1))
            else:
                print(c + column * (r - 1), end=" ")
    else:
        for c in range(1,column+1):
            if c == column:
                print(column * r + 1 - c)
            else:
                print(column * r + 1 - c, end=" ")
