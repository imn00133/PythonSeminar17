# https://blog.naver.com/PostList.nhn?from=postList&blogId=samsjang&categoryNo=80&currentPage=10
__author__ = 'samsjang@naver.com'

import pygame

WHITE = (255, 255, 255)
pad_width = 1280
pad_height = 640
background_width = 1280


def airplane(x, y):
    global gamepad, aircraft
    gamepad.blit(aircraft, (x, y))


def back(background, x, y):
    global gamepad
    gamepad.blit(background, (x, y))


def rungame():
    global gamepad, aircraft, clock, background1, backgorund2

    x = pad_width * 0.05
    y = pad_height * 0.8
    y_change = 0

    background1_x = 0
    background2_x = background_width

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        y += y_change
        gamepad.fill(WHITE)

        background1_x -= 2
        background2_x -= 2

        if background1_x == -background_width:
            background1_x = background_width

        if background2_x == -background_width:
            background2_x = background_width

        back(background1, background1_x, 0)
        back(background2, background2_x, 0)
        airplane(x, y)
        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()


def initGame():
    global gamepad, aircraft, background1, background2, clock

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('PyFlying')
    aircraft = pygame.image.load('images/plane.png')
    background1 = pygame.image.load('images/background.png')
    background2 = background1.copy()

    clock = pygame.time.Clock()
    rungame()

initGame()