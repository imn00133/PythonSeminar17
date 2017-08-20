row = int(input("행을 입력하세요: "))
column = int(input("열을 입력하세요: "))

matrix = [[0]*column for i in range(row)]
print(matrix)
count = 1
for i in range(row):
    for j in range(column):
        matrix[i][j] = count
        count += 1
        print("%3d" % matrix[i][j], end="")
    print("")
