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

# DISPLAY Surface 설정하기
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('PyFlying')

# 색
WHITE = (255, 255, 255)


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    while True: # 게임 루프
        DISPLAYSURF.fill(WHITE)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
