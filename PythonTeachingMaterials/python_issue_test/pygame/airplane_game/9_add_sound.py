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
    bat_max_catch = 0

    def __init__(self):
        global IMAGESDICT
        super().__init__()
        self.image = IMAGESDICT['airplane']
        self.rect = self.image.get_rect()
        self.rect.left = WINDOWWIDTH * 0.05
        self.rect.top = WINDOWHEIGHT * 0.8
        self.bat_catch = 0

    def change_y(self, value):
        """
        비행기의 y값을 바꾼다.
        :param value: 이동거리
        :return:
        """
        if self.rect.top + value < 0:
            self.rect.top = 0
        elif self.rect.top + value > WINDOWHEIGHT - self.image.get_height():
            self.rect.top = WINDOWHEIGHT - self.image.get_height()
        else:
            self.rect.top += value

    def change_x(self, value):
        """
        비행기의 x값을 바꾼다.
        :param value: 이동거리
        :return:
        """
        if self.rect.left + value < 0:
            self.rect.left = 0
        elif self.rect.left + value > WINDOWWIDTH - self.image.get_width():
            self.rect.left = WINDOWWIDTH - self.image.get_width()
        else:
            self.rect.left += value

    def position(self):
        """
        위치를 반환해준다.
        :return: 왼쪽 위 좌표
        """
        return self.rect.left, self.rect.top

    def bat_catch_add(self):
        self.bat_catch += 1

    def bat_catch_return(self):
        return self.bat_catch


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
    bat_remove_time = []
    bat_passed = 0

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
        또한, remove_time이 너무 붙지 않도록 짧게 잡혔을 경우 0.5초의 시간적 여유를 준다.
        :return:
        """
        BatEnemy.bat_num -= 1
        BatEnemy.bat_remove_time.append(time.time())
        if len(BatEnemy.bat_remove_time) >= 2 and \
            BatEnemy.bat_remove_time[-2]-BatEnemy.bat_remove_time[-1] < 0.1:
            BatEnemy.bat_remove_time[-1] += 0.5

    def update(self):
        """
        맨 왼쪽으로 가면 없애면서 pass를 늘린다.
        :return:
        """
        self.rect = self.rect.move(-self.BATSPEED, 0)
        if self.rect.left < 0:
            BatEnemy.bat_passed += 1
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
    """
    text surface를 만들어준다.
    :param text: 사용할 text
    :param font: 사용할 폰트 객체
    :param color: 색
    :return: surface, rect
    """
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def disp_message(sentence, pos_x, pos_y, size, color, position=""):
    """
    message를 표시해준다.
    :param sentence: 쓸 문장
    :param pos_x: x위치
    :param pos_y: y위치
    :param size: 크기(window size에 따라 조절됨)
    :param color: 색
    :param position: 위치의 기준이 왼쪽 위인지, 중앙인지 정한다. (default 왼쪽위)
    :return: None
    """
    text = pygame.font.Font('freesansbold.ttf', int(size*WINDOWWIDTH/ORIGINBACKGROUNDWIDTH))
    text_surf, text_rect = text_obj(sentence, text, color)
    if position == "center":
        text_rect.center = (pos_x, pos_y)
    else:
        text_rect.left = pos_x
        text_rect.top = pos_y
    draw_object(text_surf, text_rect.left, text_rect.top)


def game_over(bat_captured, text):
    """
    게임이 종료되면, 메세지를 출력하고, 값을 초기화 한다. top score도 계산한다.
    :param bat_captured: 지금까지 잡은 박쥐 수
    :param text: 출력 메세지
    :return:
    """
    disp_message(text, WINDOWWIDTH/2, WINDOWHEIGHT/2, 115, RED, "center")
    BatEnemy.bat_passed = 0
    # 가지고 있는 재생성 시간을 다 초기화 한다.
    del(BatEnemy.bat_remove_time[:])
    # 가끔 초기화 되지 않는 오류가 있어 명시적으로 초기화 한다.
    BatEnemy.bat_num = 0
    AirPlane.bat_max_catch = max(bat_captured, AirPlane.bat_max_catch)
    pygame.display.update()
    pygame.time.delay(2000)
    main()


def draw_bat_score(bat_captured):
    """
    왼쪽 위에 score를 출력한다.
    :param bat_captured: 잡은 박쥐 수
    :return: None
    """
    disp_message("Top Score: %d, Bat captured: %d, Bat passed: %d"
                 % (AirPlane.bat_max_catch, bat_captured, BatEnemy.bat_passed),
                 5, 5, 20, WHITE)


def recreate_bat():
    """
    BATTIME만큼의 시간이 지났는지 확인하는 함수
    시간이 지나면 박쥐를 만든다. 비어있는 경우는 check하고 들어온다.
    :return: bool
    """
    if BatEnemy.BATTIME <= time.time() - BatEnemy.bat_remove_time[0]:
        BatEnemy.bat_remove_time.pop(0)
        return True
    else:
        return False


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
    global IMAGESDICT, SOUNDSDICT

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

    # 박쥐 및 fireball 최대 개수 초기화
    bat_maximum_num = 1
    fireball_max_num = 1

    # 게임 배경음악 초기화
    pygame.mixer.music.load(SOUNDSDICT["background"])
    pygame.mixer.music.play(-1, 0.0)

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
                    SOUNDSDICT["shot"].play()
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
        if bat_maximum_num > BatEnemy.bat_num:
            if BatEnemy.bat_remove_time:
                if recreate_bat():
                    bat_group.add(BatEnemy())
                    sprite_group.add(bat_group)
            else:
                bat_group.add(BatEnemy())
                sprite_group.add(bat_group)

        # fireball 생성
        if len(fireball_group) < fireball_max_num:
            fireball_group.add(FireBall())
            sprite_group.add(fireball_group)

        # 충돌을 검사한다.
        # 박쥐와 총알의 충돌 검사
        bat_collision_dict = pygame.sprite.groupcollide(bullet_group, bat_group, False, False)
        if bat_collision_dict:
            for bullet in bat_collision_dict.keys():
                bat_x, bat_y = bat_collision_dict[bullet][0].position()
                boom_group.add(Boom(bat_x, bat_y))
                SOUNDSDICT["explosion"].play()
            sprite_group.add(boom_group)
            airplane.bat_catch_add()
            pygame.sprite.groupcollide(bullet_group, bat_group, True, True)
            # 박쥐, fireball의 숫자를 규칙에 따라 늘린다.
            if airplane.bat_catch_return() % 2 == 0:
                bat_maximum_num += 1
                BatEnemy.bat_remove_time.insert(0, time.time())
            if airplane.bat_catch_return() % 4 == 0:
                fireball_max_num += 1

        # 비행기와 박쥐, 파이어볼의 충돌 검사
        airplane_crash_bat = pygame.sprite.spritecollide(airplane, bat_group, True)
        airplane_crash_fire = pygame.sprite.spritecollide(airplane, fireball_group, True)
        if airplane_crash_bat or airplane_crash_fire:
            # group이 그냥 초기화되면, 소멸자가 작동하지 않는 것으로 보아, 객체가 남는 것으로 보인다.
            # group을 명시적으로 비워준다.
            if airplane_crash_bat:
                # 박쥐와 비행기 충돌시, 리스트로 batsprite를 넘겨줘서 bat객체가 삭제되지 않는 것으로 추정.
                del airplane_crash_bat[:]
            sprite_group.empty()
            bullet_group.empty()
            bat_group.empty()
            boom_group.empty()
            fireball_group.empty()
            SOUNDSDICT['crash'].play()
            game_over(airplane.bat_catch_return(), "Crashed!")

        # 박쥐를 잡은 개수와 넘어간 개수를 띄운다.
        draw_bat_score(airplane.bat_catch_return())

        # 박쥐가 4마리 이상 넘어가면 gameover를 출력한다.
        if BatEnemy.bat_passed >= 4:
            game_over(airplane.bat_catch_return(), "Game Over")

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
    global IMAGESDICT, SOUNDSDICT
    FPSCLOCK = pygame.time.Clock()
    pygame.init()

    # DISPLAY Surface 설정하기
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('PyFlying')
    pygame.display.set_icon(pygame.image.load('images/icon.png'))

    # 이미지 받아오기
    IMAGESDICT = {"airplane": pygame.image.load('images/plane.png'),
                  "background": pygame.image.load('images/background.png'),
                  "bat": pygame.image.load('images/bat.png'),
                  "fireball1": pygame.image.load('images/fireball.png'),
                  "fireball2": pygame.image.load('images/fireball2.png'),
                  "bullet": pygame.image.load('images/bullet.png'),
                  "boom": pygame.image.load('images/boom.png'),
                  "blank": pygame.image.load('images/blank.png')}

    # 음향 받아오기
    SOUNDSDICT = {"shot": pygame.mixer.Sound("sounds/shot.wav"),
                  "explosion": pygame.mixer.Sound("sounds/explosion.wav"),
                  "crash": pygame.mixer.Sound("sounds/airplane_crash.wav"),
                  "background": "sounds/Birds_in_Flight.mp3"}

    # 배경 이미지 게임 윈도우 크기에 맞추기
    assert WINDOWWIDTH <= ORIGINBACKGROUNDWIDTH or WINDOWHEIGHT <= ORIGINBACKGROUNDHEIGHT,\
        '게임 윈도우 크기가 너무 큽니다.'
    IMAGESDICT["background"] = pygame.transform.scale(IMAGESDICT["background"], (WINDOWWIDTH, WINDOWHEIGHT))
    main()


if __name__ == '__main__':
    game_init()
