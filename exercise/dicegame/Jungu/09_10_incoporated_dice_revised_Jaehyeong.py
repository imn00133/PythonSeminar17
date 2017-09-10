import random

regame = 1
user_number = 0
dice = 0


def det_dice():
    global user_number
    global dice
    while 1:
        user_number = int(input("정다면체의 면의 개수를 입력하시오: "))
        dice = int(input("주사위의 개수를 입력하시오: "))
        if user_number == 4 or user_number == 6 or user_number == 8 or user_number == 12 or user_number == 20:
            break
        else:
            print("다시 입력하시오")
            continue


while regame:
    det_dice()
    game_mode = int(input("게임모드를 선택하시오(1:주사위게임, 2:홀짝게임, 3:점수게임): "))
    if game_mode == 1:
        game = 0
        win = 0
        sum_of_dice = 0
        sum_of_dice_computer = 0
        game = game + 1
        for j in range(1, dice + 1):
            dice_number = []
            for i in range(1, user_number + 1):
                dice_number = dice_number + [i]
            random_number = random.choice(dice_number)
            random_number_computer = random.choice(dice_number)
            print("사용자의 %s번쨰 주사위의 눈금: %s" % (j, random_number))
            print("컴퓨터의 %s번째 주사위의 눈금: %s" % (j, random_number_computer))
            sum_of_dice = sum_of_dice + random_number
            sum_of_dice_computer = sum_of_dice_computer + random_number_computer
            if j == dice:
                print("사용자의 주사위 눈금의 총 합: %s" % sum_of_dice)
                print("컴퓨터의 주사위 눈금의 총 합: %s" % sum_of_dice_computer)
                if sum_of_dice > sum_of_dice_computer:
                    win = win + 1
                    print("사용자가 이겼습니다.")
                    print("현재까지 %s판 중 %s판 이겼습니다." % (game, win))
                elif sum_of_dice == sum_of_dice_computer:
                    print("비겼습니다.")
                else:
                    print("컴퓨터가 이겼습니다.")
        regame = int(input("다시 하시겠습니까?(1=예,0=아니오): "))
    elif game_mode == 2:
        win = 0
        game = 0
        sum_of_dice_computer = 0
        computer_dice_number = []
        game = game + 1
        for i in range(1, dice + 1):
            dice_number = []
            for j in range(1, user_number + 1):
                dice_number = dice_number + [j]
            random_number_computer = random.choice(dice_number)
            sum_of_dice_computer = sum_of_dice_computer + random_number_computer
            computer_dice_number = computer_dice_number + [random_number_computer]
        even_odd = int(input("홀수라면 1을, 짝수라면 2를 입력하세요: "))
        if sum_of_dice_computer % 2 == 0:
            if even_odd == 2:
                win = win + 1
                print("congratuation!")
                print("%s번 도전하여 %s번 맞추셨습니다." % (game, win))
            else:
                print("틀리셨습니다.")
                for a in range(1, dice + 1):
                    print("%s번째 주사위의 눈금: %s" % (a, computer_dice_number[a - 1]))
                print("총 합계는 %s 입니다" % sum_of_dice_computer)
        else:
            if even_odd == 1:
                win = win + 1
                print("congratuation!")
                print("%s번 도전하여 %s번 맞추셨습니다." % (game, win))
            else:
                print("틀리셨습니다.")
                for a in range(1, dice + 1):
                    print("%s번째 주사위의 눈금: %s" % (a, computer_dice_number[a - 1]))
                print("총 합계는 %s 입니다" % sum_of_dice_computer)
        regame = int(input("다시 하시겠습니까?(1:예, 0:아니오): "))
    elif game_mode == 3:
        user_score = int(input("사용자의 점수를 입력하시오"))
        computer_score = int(input("컴퓨터의 점수를 입력하시오"))
        while regame:
            while 1:
                for j in range(1, dice + 1):
                    dice_number = []
                    for i in range(1, user_number + 1):
                        dice_number = dice_number + [i]
                    random_number = random.choice(dice_number)
                    random_number_computer = random.choice(dice_number)
                    user_score = user_score - random_number_computer
                    computer_score = computer_score - random_number
                    print("사용자의 %s번쨰 주사위의 눈금: %s" % (j, random_number))
                    print("컴퓨터의 %s번째 주사위의 눈금: %s" % (j, random_number_computer))
                game_choice = int(input("다시 던지시겠습니까?(1:Yes,2:No,3:Change): "))
                if game_choice == 1:
                    continue
                elif game_choice == 2:
                    if user_score > computer_score:
                        print("사용자의 점수:%s, 컴퓨터의 점수:%s" % (user_score, computer_score))
                        print("사용자가 이겼습니다.")
                        regame = 0
                        break
                    elif user_score == computer_score:
                        print("사용자의 점수:%s, 컴퓨터의 점수:%s" % (user_score, computer_score))
                        print("비겼습니다.")
                        regame = 0
                        break
                    else:
                        print("사용자의 점수:%s, 컴퓨터의 점수:%s" % (user_score, computer_score))
                        print("컴퓨터가 이겼습니다.")
                        regame = 0
                        break
                else:
                    break
    else:
        print("다시 입력하시오")
