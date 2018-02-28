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
# 배경 속도
BACKGROUNDSPEED = 2
# 색
WHITE = (255, 255, 255)
RED   = (255,   0,   0)


class AirPlane(pygame.sprite.Sprite):
    """
    비행기 class
    player로 사용될 비행기이다.
    """
    def __init__(self):
        global IMAGESDICT
        super().__init__()
        self.image = IMAGESDICT['airplane']
        self.rect = self.image.get_rect()
        self.rect.left = WINDOWWIDTH * 0.05
        self.rect.top = WINDOWWIDTH * 0.8

    def change_y(self, value):
        if self.rect.top + value < 0:
            self.rect.top = 0
        elif self.rect.top + value > WINDOWHEIGHT - self.image.get_height():
            self.rect.top = WINDOWHEIGHT - self.image.get_height()
        else:
            self.rect.top += value

    def change_x(self, value):
        if self.rect.left + value < 0:
            self.rect.left = 0
        elif self.rect.left + value > WINDOWWIDTH - self.image.get_width():
            self.rect.left = WINDOWWIDTH - self.image.get_width()
        else:
            self.rect.left += value

    def position(self):
        return self.rect.left, self.rect.top


class FireBall(pygame.sprite.Sprite):
    """
    파이어 볼 class
    2/7확률로 파이어 볼이 나간다.
    없을때는 시간 지연 정책으로 2배의 속도로 아무것도 없는 파이어 볼이 움직인다.
    있을때는 파이어 볼 이미지 둘 중 하나로 움직인다.
    """
    FIREBALLSPEED = 15
    FIREBALLNUM = 1
    PROBABILITY = 7

    def __init__(self):
        global IMAGESDICT
        super().__init__()
        self.fireball_choice = random.randint(1, self.PROBABILITY)
        if self.fireball_choice <= 2:
            self.image = IMAGESDICT["fireball%s" % self.fireball_choice]
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = init_enemy_pos(self.image)
        else:
            self.image = IMAGESDICT["blank"]
            self.rect = self.image.get_rect()
            self.rect.left = WINDOWWIDTH
            self.rect.top = -2

    def update(self):
        if self.rect.left <= 0:
            self.kill()
        if self.fireball_choice <= 2:
            self.rect.left -= self.FIREBALLSPEED
        else:
            self.rect.left -= 2 * self.FIREBALLSPEED


class Boom(pygame.sprite.Sprite):
    """
    박쥐가 죽었을 때, 폭발이미지
    """
    BOOMTIME = 5

    def __init__(self, x, y):
        global IMAGESDICT
        super().__init__()
        self.image = IMAGESDICT["boom"]
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.time = 0

    def update(self):
        self.time += 1
        if self.time >= self.BOOMTIME:
            self.kill()


class BatEnemy(pygame.sprite.Sprite):
    """
    박쥐를 만드는 class
    batspeed: 이동속도
    battime: 죽었을 때 기다리는 시간
    bat_num: 박쥐의 수
    bat_remove_time: 박쥐가 제거된 시간
    """
    BATSPEED = 7
    BATTIME = 3
    bat_num = 0
    bat_remove_time = 0

    def __init__(self):
        """
        마지막에 BatEnemy class의 bat_num의 값을 변경하여 추가한다.
        """
        global IMAGESDICT
        super().__init__()
        self.image = IMAGESDICT["bat"]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = init_enemy_pos(self.image)
        BatEnemy.bat_num += 1

    def __del__(self):
        """
        BatEnemy.bat_num을 줄인다.
        :return:
        """
        BatEnemy.bat_num -= 1
        BatEnemy.bat_remove_time = time.time()

    def update(self):
        self.rect = self.rect.move(-self.BATSPEED, 0)
        if self.rect.left < 0:
            self.kill()

    def position(self):
        return self.rect.left, self.rect.top


class AirplaneBullet(pygame.sprite.Sprite):
    """
    비행기가 발사하는 총알을 저장하는 class
    기초 속도는 15이다.
    """
    BULLETSPEED = 15

    def __init__(self, airplane_xy):
        """
        생성자, 이미지는 global로 받아옴으로, 게임중에 받아오지 않으면 알 수 없는 airplane의 x, y위치만 받아온다.
        :param airplane_x: 비행기 x위치
        :param airplane_y: 비행기 y위치
        """
        global IMAGESDICT
        super().__init__()
        self.image = IMAGESDICT["bullet"]
        self.rect = self.image.get_rect()
        self.rect.left = airplane_xy[0] + IMAGESDICT["airplane"].get_width()
        self.rect.top = airplane_xy[1] + IMAGESDICT["airplane"].get_height() / 2

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


def text_obj(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def disp_message(sentence, pos_x, pos_y, size, color):
    text = pygame.font.Font('freesansbold.ttf', int(size*WINDOWWIDTH/ORIGINBACKGROUNDWIDTH))
    text_surf, text_rect = text_obj(sentence, text, color)
    text_rect.center = (pos_x, pos_y)
    draw_object(text_surf, text_rect.left, text_rect.top)


def crash():
    disp_message("Crashed!", WINDOWWIDTH/2, WINDOWHEIGHT/2, 115, RED)
    pygame.display.update()
    pygame.time.delay(2000)
    main()


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
    airplane_y_change = 0
    airplane_x_change = 0

    # 윈도우 변경에 따른 배경크기 변경
    BACKGROUNDWIDTH = IMAGESDICT["background"].get_width()

    # 배경 초기 위치
    background_x = 0
    other_background_x = BACKGROUNDWIDTH

    # 개별 sprite group
    bullet_group = pygame.sprite.Group()
    bat_group = pygame.sprite.Group()
    boom_group = pygame.sprite.Group()
    fireball_group = pygame.sprite.Group()
    # 전체 sprite group
    sprite_group = pygame.sprite.Group()

    # 비행기 sprite
    airplane = AirPlane()
    sprite_group.add(airplane)

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
                    bullet_group.add(AirplaneBullet(airplane.position()))
                    sprite_group.add(bullet_group)
            if event.type == KEYUP:
                if event.key == K_UP or event.key == K_DOWN:
                    airplane_y_change = 0
                elif event.key == K_RIGHT or event.key == K_LEFT:
                    airplane_x_change = 0
        # 누르고 있으면 비행기가 움직이는 부분이다.
        # for event 내에서는 키가 떨어지거나 붙어야지만 작동하기 때문에 밖에서 처리한다.
        airplane.change_x(airplane_x_change)
        airplane.change_y(airplane_y_change)

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
        if BatEnemy.BATTIME <= time.time() - BatEnemy.bat_remove_time \
                and BatEnemy.bat_num <= 0:
            bat_group.add(BatEnemy())
            sprite_group.add(bat_group)

        # fireball 생성
        if len(fireball_group) <= 0:
            fireball_group.add(FireBall())
            sprite_group.add(fireball_group)

        # 충돌을 검사한다.
        # 박쥐와 총알의 충돌 검사
        bat_collision_dict = pygame.sprite.groupcollide(bullet_group, bat_group, False, False)
        if bat_collision_dict:
            for bullet in bat_collision_dict.keys():
                bat_x, bat_y = bat_collision_dict[bullet][0].position()
                boom_group.add(Boom(bat_x, bat_y))
            sprite_group.add(boom_group)
            pygame.sprite.groupcollide(bullet_group, bat_group, True, True)
        # 비행기와 박쥐, 파이어볼의 충돌 검사
        airplane_crash_bat = pygame.sprite.spritecollide(airplane, bat_group, False)
        airplane_crash_fire = pygame.sprite.spritecollide(airplane, fireball_group, False)
        if airplane_crash_bat or airplane_crash_fire:
            # group이 그냥 초기화되면, 소멸자가 작동하지 않는 것으로 보아, 객체가 남는 것으로 보인다.
            # group을 명시적으로 비워준다.
            sprite_group.empty()
            bullet_group.empty()
            bat_group.empty()
            boom_group.empty()
            fireball_group.empty()
            crash()

        # 모든 sprite의 update함수를 실행한다.
        sprite_group.update()

        # 다른 스프라이트 그리기
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
                  "bullet": pygame.image.load('images/bullet.png'),
                  "boom": pygame.image.load('images/boom.png'),
                  "blank": pygame.image.load('images/blank.png')}

    # 배경 이미지 게임 윈도우 크기에 맞추기
    assert WINDOWWIDTH <= ORIGINBACKGROUNDWIDTH or WINDOWHEIGHT <= ORIGINBACKGROUNDHEIGHT,\
        '게임 윈도우 크기가 너무 큽니다.'
    IMAGESDICT["background"] = pygame.transform.scale(IMAGESDICT["background"], (WINDOWWIDTH, WINDOWHEIGHT))
    main()


if __name__ == '__main__':
    game_init()
