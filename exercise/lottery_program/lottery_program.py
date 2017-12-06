def open_file():
    """
    list파일을 연다. 첫 줄은 설명임으로 제거한다.
    :return: lottery_list
    """
    try:
        file_list = open("list.txt", "r", encoding="utf-8")
    except FileNotFoundError:
        print("list.txt 파일이 없습니다.")
    file_list.readline()
    lottery_list=[]
    while True:
        line = file_list.readline()
        if not line:
            break
        lottery_list.append(line.strip().split())
    file_list.close()
    return lottery_list


def lottery_total(lottery_list):
    """
    게임번호만 뽑아 list로 retrun해준다.
    :return: lottery_number
    """
    lottery_number = []
    for i in lottery_list:
        lottery_number.extend(i[0])
    lottery_number = sorted(list(set(lottery_number)))
    return lottery_number


# 프로그램의 시작
lottery_list = open_file()
lottery_list.sort()
lottery_number = lottery_total(lottery_list)
print(lottery_number)
print("추첨 리스트입니다.")
print("번호 이름 선택번호")
for list_line in lottery_list:
    for element in list_line:
        print("%s " % element, end="")
    print()
