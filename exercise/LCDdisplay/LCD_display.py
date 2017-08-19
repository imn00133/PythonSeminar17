def hori_output(disp_size, shape):
    hori_array=[]
    if shape=='-':
        hori_array.append(" ")
        for i in range(disp_size):
            hori_array.append("-")
        hori_array.append(" ")
    elif shape==' |':
        hori_array.append(" ")
        for i in range(disp_size):
            hori_array.append(" ")
        hori_array.append("|")
    elif shape=='| ':
        hori_array.append("|")
        for i in range(disp_size):
            hori_array.append(" ")
        hori_array.append(" ")
    elif shape=='||':
        hori_array.append("|")
        for i in range(disp_size):
            hori_array.append(" ")
        hori_array.append("|")
    else:
        hori_array.append(" ")
        for i in range(disp_size):
            hori_array.append(" ")
        hori_array.append(" ")


def change_num(display_size, num):
    display_array=[]
    if num=='0':
        for i in range(2):
            display_array.append(hori_output(display_size, '-'))
            for j in range(display_size):
                display_array.append(hori_output(display_size, '||'))
        display_array.append(hori_output(display_size,'-'))
        return display_array
    elif num=='1':
        for i in range(2):
            display_array.append(hori_output(display_size, ''))
            for j in range(display_size):
                display_array.append(hori_output(display_size, ' |'))
        display_array.append(hori_output(display_size, ''))
        return display_array
    else:
        pass
""" elif num=='2':

    elif num=='3':

    elif num=='4':

    elif num=='5':

    elif num=='6':

    elif num=='7':

    elif num=='8':
"""

while True:
    # 입력받자마자 바로 리스트로 바꿔준다.
    user_input = input("출력 값을 입력해주세요: ").split()
    user_input[0] = int(user_input[0])
    if user_input[0] == 0:
        break
    display_value=[]
    # 받는 숫자를 한 자리씩 떼서 넘긴다.
    for number in range(len(user_input[1])):
        display_value.append(change_num(user_input[0], user_input[1][number]))
        #display_value+=[""*user_input[0]]

    # 이중반복으로 출력
    for i in range(len(display_value)):
        for j in range(len(display_value[0])):
            print(display_value[i][j], end="")
        print("")