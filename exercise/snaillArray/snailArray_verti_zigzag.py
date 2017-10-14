row = int(input("행의 수를 입력하세요. "))
column = int(input("열의 수를 입력하세요. "))
array_verti = [[0]*column for i in range(row)]

number = 1
for j in range(column):
    if j % 2 == 0:
        for i in range(row):
            array_verti[i][j] = number
            number += 1
    else:
        for i in range(row-1, -1, -1):
            array_verti[i][j] = number
            number += 1

for i in range(row):
    for j in range(column):
        print("%3d "% array_verti[i][j], end=" ")
    print("")
