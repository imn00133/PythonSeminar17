import random


def dice_make():
    """
    주사위의 면을 받아 조건을 확인하는 함수
    이 부분에서 dice_face및 dice_num은 모든 함수에서 사용되야되기 때문에 전역변수를 사용할 수 밖에 없다.
    과제 잘못 만들었다...
    """
    global dice_face, dice_num
    while True:
        dice_face = int(input("주사위 면의 개수를 입력하세요: "))
        if not (dice_face == 4 or dice_face == 6
                or dice_face == 8 or dice_face == 12 or dice_face == 20):
            print("잘못 입력하셨습니다. 면의 개수는 정다면체(4, 6, 8, 12, 20)만 가능합니다.")
        else:
            break
    dice_num = int(input("주사위의 개수를 입력하세요: "))
    while dice_num <= 0:
        dice_num = int(input("주사위의 개수를 입력하세요: "))


def dice_sum(user):
    """
    주사위 사용자, 면, 개수를 받아 합을 출력해준다. 주사위 개수는 1이 초기값이다.
    마지막 합계에서는 줄바꿈을 하지 않는다.
    :param user: string 사용자 이름
    :return: int 총 계
    """
    dice_return = []
    for i in range(dice_num):
        dice_return.append(random.randint(1, dice_face))

    dice_total = 0
    for i in dice_return:
        dice_total += i

    print("%s: " % user, end="")
    for i in range(len(dice_return)):
        print("%d" % dice_return[i], end="")
        if i != len(dice_return)-1:
            print(", ", end="")
    print(" 합계: %d" % dice_total, end="")
    return dice_total


def end_flag(flag, game_win):
    """
    같은 종료방식을 쓰기 때문에 재사용한다.
    :param flag: string 이겼는지 졌는지 받아옴 win과 lose, draw가 가능하다.
    :param game_win: int 몇 번 이겼는지 받아옴
    :return: string 다시 하는지에 대해서 반환해준다.
    """
    if flag == "win":
        print("사용자가 %d번 이겼습니다." % game_win)
    elif flag == "draw":
        print("비겼습니다.")
    else:
        print("사용자가 졌습니다.")
    while True:
        exec_flag = input("다시 하시겠습니까(yes/no/change)? ")
        if exec_flag == "yes" or exec_flag == "no":
            return exec_flag
        elif exec_flag == "change":
            dice_make()


def sum_dice_game():
    """
    합계 주사위 게임, 야바위
    만일 총 이긴 횟수를 계속 카운트 하려면 game_win으로 받아온다.
    :return: int 게임의 이긴 횟수를 되돌려준다.
    """
    game_win = 0
    exec_flag = "yes"
    while exec_flag != "no":
        comp_total = dice_sum("컴퓨터")
        print("")
        user_total = dice_sum("사용자")
        print("")
        if comp_total < user_total:
            flag = "win"
            game_win += 1
        elif comp_total == user_total:
            flag = "draw"
        else:
            flag = "lose"
        exec_flag = end_flag(flag, game_win)
    return game_win


def odd_even_dice_game():
    """
    홀짝 게임
    만일 총 이긴 횟수를 계속 카운트 하려면 game_win으로 받아온다.
    :return: int 게임의 이긴 횟수를 되돌려준다.
    """
    game_win = 0
    exec_flag = "yes"
    while exec_flag != "no":
        user_choice = ""
        while user_choice != "홀" and user_choice != "짝":
            user_choice = input("홀/짝을 입력해주세요: ")
        comp_total = dice_sum("컴퓨터")
        if comp_total % 2 == 0:
            comp_value = "짝"
        else:
            comp_value = "홀"
        print("(%s)" % comp_value)
        if comp_value == user_choice:
            flag = "win"
            game_win += 1
        else:
            flag = "lose"
        exec_flag = end_flag(flag, game_win)
    return game_win


def sub_dice_game():
    """

    :return:
    """
    game_win = 0
    exec_flag = "yes"
    while exec_flag != "no":
        # 점수 설정
        user_total_score = 0
        while user_total_score <= 0:
            user_total_score = int(input("초기 점수를 입력해주세요: "))
        comp_total_score = user_total_score

        # 본 게임
        user_flag = "yes"
        while user_total_score > 0 and comp_total_score > 0 and user_flag == "yes":
            user_flag = ""
            comp_score = dice_sum("컴퓨터")
            print("")
            user_score = dice_sum("사용자")
            print("")
            if comp_score > user_score:
                print("컴퓨터가 이겼습니다.")
                user_total_score -= comp_score
            elif comp_score < user_score:
                print("사용자가 이겼습니다.")
                comp_total_score -= user_score
            else:
                print("비겼습니다.")
            print("현재 점수는 컴퓨터: %d, 사용자: %d 입니다." % (comp_total_score, user_total_score))
            while user_flag != "yes" and user_flag != "no" and user_total_score > 0 and comp_total_score > 0:
                user_flag = input("다시 던지시겠습니까(yes/no/change): ")
                if user_flag == "change":
                    dice_make()

        if comp_total_score < user_total_score:
            flag = "win"
            game_win += 1
        elif comp_total_score == user_total_score:
            flag = "draw"
        else:
            flag = "lose"
        exec_flag = end_flag(flag, game_win)
    return game_win

# dice_face 및 dice_num는 전역변수로 사용된다. dice_make가 언제든 사용될 수 있기 때문에 어쩔 수 없다.
# dice_num을 전역변수로 사용하지 않게 했었어야 되었는데... 잘못 만들었다.
# 주사위 다른 것을 여러 개 만든다면 어떤 일들이... 답은 객체지향인가보다.

# 주사위 만들기
dice_face = dice_num = 0
dice_make()

# 프로그램의 시작
game_list = ["주사위 합계 게임", "주사위 홀짝 게임", "주사위 뺄셈 게임"]
user_choice_game = 0
sum_dice_game_win = odd_even_game_win = sub_dice_game_win = 0
while True:
    while user_choice_game <= 0 or user_choice_game > len(game_list):
        print("주사위 게임 프로그램을 시작합니다.")
        # 확장성을 위해 게임리스트를 리스트로 만들고 출력한다.
        for i in range(len(game_list)):
            print("%d. %s" % (i + 1, game_list[i]))
        user_choice_game = input("선택해주세요(exit를 입력하면 종료됩니다.): ")
        if user_choice_game == "exit":
            break
        else:
            user_choice_game = int(user_choice_game)

    # 게임 선택 창
    if user_choice_game == 1:
        sum_dice_game_win += sum_dice_game()
    elif user_choice_game == 2:
        odd_even_game_win += odd_even_dice_game()
    elif user_choice_game == 3:
        sub_dice_game_win += sub_dice_game()
    elif user_choice_game == "exit":
        print("사용자는 주사위 합계 게임을 %d번, 홀짝게임을 %d번, 뺄셈게임을 %d번 이겼습니다."
              % (sum_dice_game_win, odd_even_game_win, sub_dice_game_win))
        print("게임을 종료합니다.")
        break
    # 종료하기전 초기화
    user_choice_game = 0
