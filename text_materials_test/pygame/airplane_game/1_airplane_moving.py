# https://blog.naver.com/PostList.nhn?from=postList&blogId=samsjang&categoryNo=80&currentPage=10
# revision Jaehyeong Kim

import pygame
import sys
from pygame.locals import *

FPS = 30 # 초당 프레임 수
WINDOWWIDTH = 1024
WINDOWHEIGHT = 512

fpsClock = pygame.time.Clock()

# 윈도우 설정하기
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.update()
    fpsClock.tick(FPS)


while True: # 게임 루프
    DISPLAYSURF.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


