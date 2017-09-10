Matrix = []
RowNum = int(input("Row Number : "))
ColumnNum = int(input("Column Number : "))
LineIndex = 0
for i in range(0, ColumnNum):
    MatrixRow = []
    Number = 1
    for j in range(0, RowNum):
        if LineIndex%2 == 0:
            MatrixRow.append(Number+(RowNum*LineIndex))
        else:
            MatrixRow.append(RowNum*(LineIndex+1)-Number+1)
        Number = Number+ 1
    LineIndex = LineIndex + 1
    Matrix.append(MatrixRow)
for i in range(0, ColumnNum):
    for j in range(0, RowNum):
        print(Matrix[i][j], end=" ")
    print("")
