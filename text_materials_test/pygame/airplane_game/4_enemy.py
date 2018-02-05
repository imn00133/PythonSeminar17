# https://blog.naver.com/PostList.nhn?from=postList&blogId=samsjang&categoryNo=80&currentPage=10
# revision Jaehyeong Kim

import pygame
import sys
import random
import time
from pygame.locals import *

# 상수영역
# 초당 프레임 수
FPS = 30
# 윈도우 크기, 비율 일정하게 만듦
WINDOWWIDTH = 1080
WINDOWHEIGHT = int(WINDOWWIDTH / 2)
# 배경 최대 크기
ORIGINBACKGROUNDWIDTH = 1280
ORIGINBACKGROUNDHEIGHT = 640
# 스프라이트 속도
BACKGROUNDSPEED = 2
BATSPEED = 7
FIREBALLSPEED = 15
# 박쥐 재시작 시간
BATTIME = 8
# 색
WHITE = (255, 255, 255)


def init_enemy(image):
    x = WINDOWWIDTH
    y = random.randrange(0, WINDOWHEIGHT - image.get_height())
    return x, y


def draw_object(image, x, y):
    global DISPLAYSURF
    DISPLAYSURF.blit(image, (x, y))


def main():
    global FPSCLOCK, DISPLAYSURF
    global IMAGESDICT

    # 비행기 왼쪽 초기 위치
    airplane_x = WINDOWWIDTH * 0.05
    airplane_y = WINDOWHEIGHT * 0.8
    airplane_y_change = 0
    airplane_x_change = 0

    # 비행기 크기
    AIRPLANEWIDTH = IMAGESDICT["airplane"].get_width()
    AIRPLANEHEIGHT = IMAGESDICT["airplane"].get_height()

    # 윈도우 변경에 따른 배경크기 변경
    BACKGROUNDWIDTH = IMAGESDICT["background"].get_width()

    # 배경 초기 위치
    background_x = 0
    other_background_x = BACKGROUNDWIDTH

    # 박쥐 초기 위치
    bat_x, bat_y = init_enemy(IMAGESDICT["bat"])

    # 박쥐 초기화 시간변수
    bat_remove_time = 0

    # 파이어볼 초기화 및 초기 위치
    # 1/7확률로 fireball이 날아간다.
    fireball_choice = random.randint(1, 7)
    if fireball_choice == 1 or fireball_choice == 2:
        fireball_x, fireball_y = init_enemy(IMAGESDICT["fireball%s" % fireball_choice])
    else:
        fireball_x, fireball_y = WINDOWWIDTH, 0

    # game loop
    while True:
        # event handle
        for event in pygame.event.get():
            # 종료
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    airplane_y_change = -5
                elif event.key == K_DOWN:
                    airplane_y_change = 5
                if event.key == K_RIGHT:
                    airplane_x_change = 5
                elif event.key == K_LEFT:
                    airplane_x_change = -5
            if event.type == KEYUP:
                if event.key == K_UP or event.key == K_DOWN:
                    airplane_y_change = 0
                elif event.key == K_RIGHT or event.key == K_LEFT:
                    airplane_x_change = 0

        # event에 따른 비행기 위치 변경 및 제한
        airplane_y += airplane_y_change
        if airplane_y < 0:
            airplane_y = 0
        elif airplane_y > WINDOWHEIGHT - AIRPLANEHEIGHT:
            airplane_y = WINDOWHEIGHT - AIRPLANEHEIGHT

        airplane_x += airplane_x_change
        if airplane_x < 0:
            airplane_x = 0
        elif airplane_x > WINDOWWIDTH - AIRPLANEWIDTH:
            airplane_x = WINDOWWIDTH - AIRPLANEWIDTH

        # 배경 위치 설정
        background_x -= BACKGROUNDSPEED
        if background_x == -BACKGROUNDWIDTH:
            background_x = BACKGROUNDWIDTH
        draw_object(IMAGESDICT["background"], background_x, 0)

        other_background_x -= BACKGROUNDSPEED
        if other_background_x == -BACKGROUNDWIDTH:
            other_background_x = BACKGROUNDWIDTH
        draw_object(IMAGESDICT["background"], other_background_x, 0)

        # 박쥐 위치 설정
        bat_x -= BATSPEED
        if bat_x <= 0 and BATTIME <= time.time()-bat_remove_time:
            bat_remove_time = time.time()
            bat_x, bat_y = init_enemy(IMAGESDICT["bat"])

        # fireball 위치 설정
        if fireball_choice == 1 or fireball_choice == 2:
            fireball_x -= FIREBALLSPEED
        else:
            fireball_x -= 2 * FIREBALLSPEED

        if fireball_x <= 0:
            fireball_choice = random.randint(1, 7)
            if fireball_choice == 1 or fireball_choice == 2:
                fireball_x, fireball_y = init_enemy(IMAGESDICT["fireball%s" % fireball_choice])
            else:
                fireball_x, fireball_y = WINDOWWIDTH, 0

        # 다른 스프라이트 그리기
        draw_object(IMAGESDICT["airplane"], airplane_x, airplane_y)
        draw_object(IMAGESDICT["bat"], bat_x, bat_y)
        if fireball_choice == 1 or fireball_choice == 2:
            draw_object(IMAGESDICT["fireball%s" % fireball_choice], fireball_x, fireball_y)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def game_init():
    global FPSCLOCK, DISPLAYSURF
    global IMAGESDICT
    FPSCLOCK = pygame.time.Clock()
    pygame.init()

    # DISPLAY Surface 설정하기
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('PyFlying')

    # 이미지 받아오기
    IMAGESDICT = {"airplane": pygame.image.load('images/plane.png'),
                  "background": pygame.image.load('images/background.png'),
                  "bat": pygame.image.load('images/bat.png'),
                  "fireball1": pygame.image.load('images/fireball.png'),
                  "fireball2": pygame.image.load('images/fireball2.png')}

    # 배경 이미지 게임 윈도우 크기에 맞추기
    assert WINDOWWIDTH <= ORIGINBACKGROUNDWIDTH or WINDOWHEIGHT <= ORIGINBACKGROUNDHEIGHT,\
        '게임 윈도우 크기가 너무 큽니다.'
    IMAGESDICT["background"] = pygame.transform.scale(IMAGESDICT["background"], (WINDOWWIDTH, WINDOWHEIGHT))
    main()


if __name__ == '__main__':
    game_init()
