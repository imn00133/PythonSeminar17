RowNum=int(input("Row: "))          #열
ColumnNum=int(input("Column: "))    #행
Max = RowNum*ColumnNum              #숫자 몇까지 입력될 것인가
for Matrix in range(1,Max+1):       #print(Matrix)로 1~Max까지 입력되도록
    if Max%RowNum==0:               #RowNum==0 일때는 행을 바꾼다.
        print(str(Matrix)+"\n")        #\n으로 행을 바꿈
    else:
        print(str(Matrix)+" ")               #그게 아니면 그냥 출력