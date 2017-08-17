# 빈 배열 생성
def clear_matrix(size):
    Matrix = []
    MatrixColumn = []
    for i in range(0, size*2+3):
        for j in range(0, size+2):
            MatrixColumn.append(" ")
        Matrix.append(MatrixColumn)
        MatrixColumn = []
    return Matrix

# 1줄 공백
def VoidLine(size):
    MatrixVoid = []
    MatrixColumn = []
    for i in range(0, size*2+3):
        MatrixVoid.append(MatrixColumn)
    return MatrixVoid

# 1 표현하기
def ONE(size, Matrix):
    for j in range(1, size*2+2):
        Matrix[j][size+1] = "|"
    return Matrix

# 2 표현하기
def TWO(size, Matrix):
    for i in range(1, size+1):
        Matrix[0][i] = '-'
        Matrix[size+1][i] = '-'
        Matrix[size*2+2][i] = '-'
    for i in range(0, size):
        Matrix[i+1][size+1] = "|"
        Matrix[i+size+2][0] = "|"
    return Matrix

# 3 표현하기
def THREE(size, Matrix):
    for i in range(1, size+1):
        Matrix[0][i] = '-'
        Matrix[size+1][i] = '-'
        Matrix[size*2+2][i] = '-'
    for i in range(0, size):
        Matrix[i+1][size+1] = "|"
        Matrix[i+size+2][size+1] = "|"
    return Matrix

# 4 표현하기
def FOUR(size, Matrix):
    for i in range(1, size+1):
        Matrix[size+1][i] = '-'
    for i in range(0, size):
        Matrix[i+1][size+1] = "|"
        Matrix[i+1][0]="|"
        Matrix[i+size+2][size+1] = "|"
    return Matrix

# 5 표현하기
def FIVE(size, Matrix):
    for i in range(1, size+1):
        Matrix[0][i] = '-'
        Matrix[size+1][i] = '-'
        Matrix[size*2+2][i] = '-'
    for i in range(0, size):
        Matrix[i+1][0] = "|"
        Matrix[i+size+2][size+1] = "|"
    return Matrix

# 6 표현하기
def SIX(size, Matrix):
    for i in range(1, size+1):
        Matrix[0][i] = '-'
        Matrix[size+1][i] = '-'
        Matrix[size*2+2][i] = '-'
    for i in range(0, size):
        Matrix[i+1][0] = "|"
        Matrix[i+size+2][0] = "|"
        Matrix[i + size + 2][size+1] = "|"
    return Matrix

# 7 표현하기
def SEVEN(size, Matrix):
    for i in range(1, size+1):
        Matrix[0][i] = '-'
    for i in range(0, size):
        Matrix[i+1][size+1] = "|"
        Matrix[i+size+2][size+1] = "|"
    return Matrix

# 8 표현하기
def EIGHT(size, Matrix):
    for i in range(1, size+1):
        Matrix[0][i] = '-'
        Matrix[size+1][i] = '-'
        Matrix[size*2+2][i] = '-'
    for i in range(0, size):
        Matrix[i+1][0] = "|"
        Matrix[i+1][size+1] = "|"
        Matrix[i+size+2][0] = "|"
        Matrix[i + size + 2][size+1] = "|"
    return Matrix

# 9 표현하기
def NINE(size, Matrix):
    for i in range(1, size+1):
        Matrix[0][i] = '-'
        Matrix[size+1][i] = '-'
        Matrix[size*2+2][i] = '-'
    for i in range(0, size):
        Matrix[i+1][0] = "|"
        Matrix[i+1][size+1] = "|"
        Matrix[i + size + 2][size+1] = "|"
    return Matrix

# 0 표현하기
def ZERO(size, Matrix):
    for i in range(1, size+1):
        Matrix[0][i] = '-'
        Matrix[size*2+2][i] = '-'
    for i in range(0, size):
        Matrix[i+1][0] = "|"
        Matrix[i+1][size+1] = "|"
        Matrix[i+size+2][0] = "|"
        Matrix[i + size + 2][size+1] = "|"
    return Matrix

# 메트릭스 합치기
def CombineMat(Matrix_base, Matrix_add):
    NewMatrix = []
    Void = [" "]
    for i in range(0, len(Matrix_base)):
        NewMatrix.append(Matrix_base[i] + Void + Matrix_add[i])
    return NewMatrix

# 출력 명령
def draw(Matrix_todraw):
    for i in range(0, len(Matrix_todraw)):
        for j in range(0, len(Matrix_todraw[0])):
            print(Matrix_todraw[i][j], end="")
        print(" ")

# 각 함수 호출
def CallNum(Number, size, Matrix):
    if Number == '0':
        return ZERO(size, Matrix)
    elif Number == '1':
        return ONE(size, Matrix)
    elif Number == '2':
        return TWO(size, Matrix)
    elif Number == '3':
        return THREE(size, Matrix)
    elif Number == '4':
        return FOUR(size, Matrix)
    elif Number == '5':
        return FIVE(size, Matrix)
    elif Number == '6':
        return SIX(size, Matrix)
    elif Number == '7':
        return SEVEN(size, Matrix)
    elif Number == '8':
        return EIGHT(size, Matrix)
    else:
        return NINE(size, Matrix)


"""
draw(ONE(NumberSize, clear_Matrix(NumberSize)))
print("")
draw(TWO(NumberSize, clear_Matrix(NumberSize)))
print("")
draw(THREE(NumberSize, clear_Matrix(NumberSize)))
print("")
draw(FOUR(NumberSize, clear_Matrix(NumberSize)))
print("")
draw(FIVE(NumberSize, clear_Matrix(NumberSize)))
print("")
draw(SIX(NumberSize, clear_Matrix(NumberSize)))
print("")
draw(SEVEN(NumberSize, clear_Matrix(NumberSize)))
print("")
draw(EIGHT(NumberSize, clear_Matrix(NumberSize)))
print("")
draw(NINE(NumberSize, clear_Matrix(NumberSize)))
print("")
draw(ZERO(NumberSize, clear_Matrix(NumberSize)))
print("")
"""
# 파일 읽어오기
def FileReading():
    ReturnList = []
    f = open("InputLCD.txt", "r")
    while True:
        line = f.readline()
        if not line:
            break
        else:
            translate = list(line)
            translate[1:2]=[]
            size = (int(translate[0:1][0]))
            NumList = translate[1:len(translate)]
            for i in NumList:
                if i == '\n':
                    del NumList[NumList.index("\n")]
            ReturnList.append((size, NumList))
    f.close()
    return ReturnList

UserChoice = input("File input? yes / no\n")
if UserChoice == "yes":
    for i in range(0, len(FileReading())):
        (NumberSize, NumberList) = FileReading()[i]
        if NumberSize == 0 and NumberList[0] == '0' and len(NumberList) == 0:
            break
        else:
            Add = CallNum(NumberList[0], NumberSize, clear_matrix(NumberSize))
            del NumberList[0]
            for i in NumberList:
                Add = CombineMat(Add, CallNum(i, NumberSize, clear_matrix(NumberSize)))
            draw(Add)
else:
    NumberSize = int(input("Number Size?: "))
    Number = input("Number to print?: ")
    NumberList = list(Number)
    if NumberSize == 0 and NumberList[0] == '0' and len(NumberList) == 0:
        print("Program Off")
    else:
        Add = CallNum(NumberList[0], NumberSize, clear_matrix(NumberSize))
        del NumberList[0]
        for i in NumberList:
            Add = CombineMat(Add, CallNum(i, NumberSize, clear_matrix(NumberSize)))
        draw(Add)