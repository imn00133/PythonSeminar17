# https://blog.naver.com/PostList.nhn?from=postList&blogId=samsjang&categoryNo=80&currentPage=10
# revision Jaehyeong Kim

import pygame
import sys
from pygame.locals import *

# 초당 프레임 수
FPS = 30

# 윈도우 크기
WINDOWWIDTH = 1280
WINDOWHEIGHT = 640

# 색
WHITE = (255, 255, 255)


def main():
    global FPSCLOCK, DISPLAYSURF
    global AIRCRAFT

    # 비행기 왼쪽 초기 위치
    airplaneX = WINDOWWIDTH * 0.05
    airplaneY = WINDOWHEIGHT * 0.8
    airplaneY_change = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    airplaneY_change = -5
                elif event.key == K_DOWN:
                    airplaneY_change = 5
            if event.type == KEYUP:
                if event.key == K_UP or event.key == K_DOWN:
                    airplaneY_change = 0

        airplaneY += airplaneY_change
        DISPLAYSURF.fill(WHITE)
        drawobject(AIRCRAFT, airplaneX, airplaneY)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def gameinit():
    global FPSCLOCK, DISPLAYSURF
    global AIRCRAFT
    FPSCLOCK = pygame.time.Clock()
    pygame.init()

    # DISPLAY Surface 설정하기
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('PyFlying')

    # 이미지 받아오기
    AIRCRAFT = pygame.image.load('images/plane.png')

    main()


def drawobject(image, x, y):
    global DISPLAYSURF
    DISPLAYSURF.blit(image, (x, y))


if __name__ == '__main__':
    gameinit()
