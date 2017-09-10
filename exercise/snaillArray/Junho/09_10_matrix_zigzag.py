RowNum=int(input("몇 행?"))
ColumnNum=int(input("몇 열?"))
MatrixRow=[]
MatrixColumn=[]
for i in range(0, RowNum):
    for j in range(0, ColumnNum):
        MatrixColumn.append(j)
    MatrixRow.append(MatrixColumn)
    MatrixColumn = []
InNum = 0
for i in range(0, RowNum):
    for j in range(0,ColumnNum):
        if i%2==0:
            InNum+=1
            MatrixRow[i][j]=ColumnNum*i+InNum
        else:
            InNum-=1
            MatrixRow[i][j]=ColumnNum*i+InNum+1
for i in range(0,RowNum):
    for j in range(0,ColumnNum):
        print(MatrixRow[i][j], end=" ")
    print("")