row = int(input("행을 입력하세요: "))
column = int(input("열을 입력하세요: "))

array_hori = [[0]*column for i in range(row)]

index = 1
for i in range(row):
    if i % 2 == 0:
        for j in range(column):
            array_hori[i][j] = index
            index += 1
    else:
        for j in range(column-1, -1, -1):
            array_hori[i][j] = index
            index += 1

for i in range(row):
    for j in range(column):
        print("%2d" % array_hori[i][j], end=" ")
    print("")
