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
    while dice_num <= 0:
        dice_num = int(input("주사위의 개수를 입력하세요: "))


def dice_sum(user):
    """
    주사위 사용자, 면, 개수를 받아 합을 출력해준다. 주사위 개수는 1이 초기값이다.
    :param user: string 사용자 이름
    :param dice_num: int 주사위 개수
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
    print(" 합계: %d" % dice_total)
    return dice_total


def sum_dice_game(game_win):

    return game_win


def odd_even_dice_game(game_win):

    return game_win


# dice_face 및 dice_num는 전역변수로 사용된다. dice_make가 언제든 사용될 수 있기 때문에 어쩔 수 없다.
# dice_num을 전역변수로 사용하지 않게 했었어야 되었는데... 잘못 만들었다.
# 주사위 다른 것을 여러 개 만든다면 어떤 일들이... 답은 객체지향인가보다.

# 주사위 만들기
dice_face = dice_num = 0
dice_make()

# 프로그램의 시작
game_list = ["주사위 합계 게임", "주사위 홀짝 게임"]
user_choice_game = 0
sum_dice_game_win = odd_even_game_win = 0
while True:
    while user_choice_game <= 0 or user_choice_game > len(game_list):
        print("주사위 게임 프로그램을 시작합니다.")
        # 확장성을 위해 게임리스트를 리스트로 만들고 출력한다.
        for i in range(len(game_list)):
            print("%d. %s" % (i + 1, game_list[i]))
        user_choice_game = int(input("선택해주세요(exit를 입력하면 종료됩니다.): "))
        if str(user_choice_game) == "exit":
            break

    if user_choice_game == 1:
        sum_dice_game_win += sum_dice_game(sum_dice_game_win)
    elif user_choice_game == 2:
        odd_even_game_win += odd_even_dice_game(odd_even_game_win)
    elif user_choice_game == "exit":
        print("사죵자는 주사위 합계 게임을 %d번, 홀짝게임을 %d번 이겼습니다." % (sum_dice_game_win, odd_even_game_win))
        print("게임을 종료합니다.")
