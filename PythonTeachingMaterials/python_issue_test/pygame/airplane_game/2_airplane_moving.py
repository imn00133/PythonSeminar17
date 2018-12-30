# https://blog.naver.com/PostList.nhn?from=postList&blogId=samsjang&categoryNo=80&currentPage=10
# revision Jaehyeong Kim

import pygame
import sys
from pygame.locals import *

# 상수영역
# 초당 프레임 수
FPS = 30
# 윈도우 크기
WINDOWWIDTH = 1280
WINDOWHEIGHT = 640
# 배경 크기
BACKGROUNDWIDTH = 1280
BACKGROUNDHEIGHT = 640
# 색
WHITE = (255, 255, 255)


def draw_object(image, x, y):
    global DISPLAYSURF
    DISPLAYSURF.blit(image, (x, y))


def main():
    global FPSCLOCK, DISPLAYSURF
    global AIRPLANE

    # 비행기 왼쪽 초기 위치
    airplane_x = WINDOWWIDTH * 0.05
    airplane_y = WINDOWHEIGHT * 0.8
    airplane_y_change = 0
    airplane_x_change = 0

    # 비행기 크기
    AIRPLANEWIDTH = AIRPLANE.get_width()
    AIRPLANEHEIGHT = AIRPLANE.get_height()

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

        # 배경 그리기
        DISPLAYSURF.fill(WHITE)

        # 다른 스프라이트 그리기
        draw_object(AIRPLANE, airplane_x, airplane_y)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def game_init():
    global FPSCLOCK, DISPLAYSURF
    global AIRPLANE
    FPSCLOCK = pygame.time.Clock()
    pygame.init()

    # DISPLAY Surface 설정하기
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('PyFlying')

    # 이미지 받아오기
    AIRPLANE = pygame.image.load('images/plane.png')

    main()


if __name__ == '__main__':
    game_init()
