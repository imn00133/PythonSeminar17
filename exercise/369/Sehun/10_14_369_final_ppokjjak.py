#1에서 10000까지의 자연수의 각 자릿수에  3,9가 있으면 짝을, 6이 있으면 뽁짝을, 2,4,8은 뽁을 출력한다.
#단, 순서를 지킨다.

count=0  #문자를 쓸지 숫자를 쓸지 판단하기 위함
dictionary = {}  #각 숫자의 모든 자리를 검사해서 자리번호가 key, 표시할 대상이 value인 순서쌍을 저장한다.
while True:
    max = int(input("숫자를 입력하세요 : "))
    if max <1 or max >10000: #말은 이렇게 했지만 이것만 지우면 모든 자연수를 다 할 수 있다. 나도 내가 두렵다. 나란 녀석...
        print("1이상 10000이하의 숫자만 입력할 수 있습니다.")
    else:  # max가 유효한 범위의 숫자라면,
        for number in range(1,max+1):
            number_of_number = len(str(number)) #자릿수를 number_of_number에 저장
            if number%20 == 0 or number == max:  #줄바꿈을 해야하는 숫자들이라면,
                number = str(number)
                for i in range(0, number_of_number):  #0번 자리부터 최대 4번 자리까지 각각의 숫자를 검사한다
                    if number[i] in ["3", "9"]:  #i번자리 숫자가 3,9면 순서쌍 {i : "짝"} 을 dictionary에 저장
                        dictionary[i] = "짝"
                        count = count + 1
                    elif number[i] == "6":  #i번자리 숫자가 6이면 순서쌍 {i : "뽁짝"} 을 dictionary에 저장
                        dictionary[i] = "뽁짝"
                        count = count + 1
                    elif number[i] in ["2", "4", "8"]:  #i번자리 숫자가 2,4,8이면 순서쌍 {i : "뽁"} 을 dictionary에 저장
                        dictionary[i] = "뽁"
                        count = count + 1
                    else:  #i번자리 숫자가 1,5,7이면 순서쌍 {i : ""} 을 dictionary에 저장(특징없는 숫자는 count세지 않는다)
                        dictionary[i] = ""
                if count == 0:  #그냥 숫자 출력
                    print(number) #줄바꿈 한다
                else:
                    for i in range(0, number_of_number):  #dictionary에 저장했던 key들을 순서대로 불러온다
                        print(dictionary[i], end="")
                    print("") #줄바꿈 한다
                dictionary={}  #다음 number의 검사를 위해 dictionary와 count를 비워둔다
                count=0
            else:  #줄바꿈을 하지 않아야 하는 숫자들이라면,
                number = str(number)
                for i in range(0, number_of_number):
                    if number[i] in ["3", "9"]:
                        dictionary[i] = "짝"
                        count = count + 1
                    elif number[i] == "6":
                        dictionary[i] = "뽁짝"
                        count = count + 1
                    elif number[i] in ["2", "4", "8"]:
                        dictionary[i] = "뽁"
                        count = count + 1
                    else:
                        dictionary[i] = ""
                if count == 0:
                    print(number, end=" ") #줄바꿈 안하고 띄어쓰기 한번 한다
                else:
                    for i in range(0, number_of_number):
                        print(dictionary[i], end="")
                    print("", end=" ") #줄바꿈 안한고 띄어쓰기 한번 한다
                dictionary = {}
                count = 0