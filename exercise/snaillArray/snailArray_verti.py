row = int(input("행의 수를 입력하세오.: "))
column = int(input("열의 수를 입력하세오.: "))
array_verti = [[0]*column for i in range(row)]

number = 1
for j in range(column):
    for i in range(row):
        array_verti[i][j] = number
        number += 1

for i in range(row):
    for j in range(column):
        print("%3d "% array_verti[i][j], end=" ")
    print("")
