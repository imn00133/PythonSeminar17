row = int(input("행을 입력하세요: "))
column = int(input("열을 입력하세요: "))

array = [[0] * column for i in range(row)]
# 이 방법 외에도 [[0 for cols in range(column)] for rows in range(row)로 가능하다.

row_start, column_start, num, exit_num = 0, 0, 1, row * column + 1
while num != exit_num:
    # 열을 증가하며 숫자를 채워나감, 앞 쪽 행은 채워서 삭제
    for j in range(column_start, column):
        array[row_start][j] = num
        num += 1
    row_start += 1
    if num == exit_num:
        break
    # 행을 증가하며 숫자를 채워나감, 뒤 쪽 열은 채워서 삭제
    for i in range(row_start, row):
        array[i][column - 1] = num
        num += 1
    column -= 1
    if num == exit_num:
        break
    # range(start, end, step): 스타트를 포함, end를 포함안함, step만큼 이동
    for j in range(column - 1, column_start - 1, -1):
        array[row - 1][j] = num
        num += 1
    row -= 1
    if num == exit_num:
        break
    for i in range(row - 1, row_start - 1, -1):
        array[i][column_start] = num
        num += 1
    column_start += 1
    # 마지막 탈출조건은 while에서 빠짐

# 배열 출력
for i in range(len(array)):
    for j in range(len(array[0])):
        print("%3d " % array[i][j], end="")
    print("")
