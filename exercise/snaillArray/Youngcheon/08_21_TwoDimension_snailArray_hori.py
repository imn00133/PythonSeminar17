RowNum = int(input("Row: "))
ColumnNum = int(input("Column: "))
Matrix = []
for i in range(0, RowNum):
    MatrixColumn = []
    for j in range(0, ColumnNum):
        MatrixColumn.append(j+1+ColumnNum*(i))
    Matrix.append(MatrixColumn)
for i in range(0, RowNum):
    for j in range(0, ColumnNum):
        print(Matrix[i][j], end=" ")
    print("")
