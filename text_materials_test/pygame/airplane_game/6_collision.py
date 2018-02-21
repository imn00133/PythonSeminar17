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
FIREBALLSPEED = 15
# 색
WHITE = (255, 255, 255)


class BatEnemy(pygame.sprite.Sprite):
    BATSPEED = 7
    BATTIME = 3
    bat_num = 0
    bat_remove_time = 0

    def __init__(self):
        global IMAGESDICT
        pygame.sprite.Sprite.__init__(self)
        self.image = IMAGESDICT["bat"]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = init_enemy_pos(IMAGESDICT["bat"])
        self.rect2 = self.image.get_rect()
        BatEnemy.bat_num += 1
        print("나옴")

    def __del__(self):
        BatEnemy.bat_num -= 1
        BatEnemy.bat_remove_time = time.time()

    def update(self):
        self.rect = self.rect.move(-self.BATSPEED, 0)
        if self.rect.left < 0:
            self.kill()


class AirplaneBullet(pygame.sprite.Sprite):
    """
    비행기가 발사하는 총알을 저장하는 class
    """
    BULLETSPEED = 15

    def __init__(self, airplane_x, airplane_y):
        """
        생성자, 이미지는 global로 받아옴으로, 게임중에 받아오지 않으면 알 수 없는 airplane의 x, y위치만 받아온다.
        :param airplane_x: 비행기 x위치
        :param airplane_y: 비행기 y위치
        """
        global IMAGESDICT
        pygame.sprite.Sprite.__init__(self)
        self.image = IMAGESDICT["bullet"]
        self.rect = self.image.get_rect()
        self.rect.left = airplane_x + IMAGESDICT["airplane"].get_width()
        self.rect.top = airplane_y + IMAGESDICT["airplane"].get_height() / 2

    def __del__(self):
        print("죽음!!")

    def update(self):
        """
        sprite의 update를 사용하기 위해 override했다.
        class변수(상수)인 BULLETSPEED를 통해 이동한다.
        위치가 벗어나면 삭제한다.
        :return: None
        """
        self.rect = self.rect.move(self.BULLETSPEED, 0)
        if self.rect.left > WINDOWWIDTH:
            self.kill()
            print("죽음!")


def init_enemy_pos(image):
    """
    적의 초기 위치를 반환해준다.
    :param image: surface
    :return: x, y
    """
    x = WINDOWWIDTH
    y = random.randrange(0, WINDOWHEIGHT - image.get_height())
    return x, y


def draw_object(image, x, y):
    """
    surface를 display surface에 그려준다.
    :param image: surface
    :param x: x위치
    :param y: y위치
    :return: None
    """
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

    # 파이어볼 초기화 및 초기 위치
    # 2/7확률로 fireball이 날아간다.
    fireball_choice = random.randint(1, 7)
    if fireball_choice == 1 or fireball_choice == 2:
        fireball_x, fireball_y = init_enemy_pos(IMAGESDICT["fireball%s" % fireball_choice])
    else:
        fireball_x, fireball_y = WINDOWWIDTH, 0

    # 총알 sprite group
    bullet_group = pygame.sprite.Group()
    bat_group = pygame.sprite.Group()
    # 전체 sprite group
    sprite_group = pygame.sprite.Group()

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
                if event.key == K_LCTRL:
                    # 총알을 추가한다.
                    bullet_group.add(AirplaneBullet(airplane_x, airplane_y))
                    sprite_group.add(bullet_group)
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

        # 박쥐가 죽으면 재시작 시간 이후 박쥐를 만든다.
        if BatEnemy.BATTIME <= time.time()-BatEnemy.bat_remove_time\
                and BatEnemy.bat_num <= 0:
            bat_group.add(BatEnemy())
            sprite_group.add(bat_group)

        # fireball 위치 설정
        if fireball_choice == 1 or fireball_choice == 2:
            fireball_x -= FIREBALLSPEED
        else:
            fireball_x -= 2 * FIREBALLSPEED

        if fireball_x <= 0:
            fireball_choice = random.randint(1, 7)
            if fireball_choice == 1 or fireball_choice == 2:
                fireball_x, fireball_y = init_enemy_pos(IMAGESDICT["fireball%s" % fireball_choice])
            else:
                fireball_x, fireball_y = WINDOWWIDTH, 0

        # bullet과 박쥐를 포함한 모든 sprite의 update함수를 실행한다.
        sprite_group.update()

        # 충돌을 검사한다.
        bullet_hit_list = pygame.sprite.groupcollide(bat_group, bullet_group, True, True)

        # 다른 스프라이트 그리기
        draw_object(IMAGESDICT["airplane"], airplane_x, airplane_y)
        if fireball_choice == 1 or fireball_choice == 2:
            draw_object(IMAGESDICT["fireball%s" % fireball_choice], fireball_x, fireball_y)
        sprite_group.draw(DISPLAYSURF)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def game_init():
    """
    게임에 필요한 각종 값을 초기화 한다.
    :return: None
    """
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
                  "fireball2": pygame.image.load('images/fireball2.png'),
                  "bullet": pygame.image.load('images/bullet.png')}

    # 배경 이미지 게임 윈도우 크기에 맞추기
    assert WINDOWWIDTH <= ORIGINBACKGROUNDWIDTH or WINDOWHEIGHT <= ORIGINBACKGROUNDHEIGHT,\
        '게임 윈도우 크기가 너무 큽니다.'
    IMAGESDICT["background"] = pygame.transform.scale(IMAGESDICT["background"], (WINDOWWIDTH, WINDOWHEIGHT))
    main()


if __name__ == '__main__':
    game_init()
