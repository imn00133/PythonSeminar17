# pip install pygame으로 pygame을 설치하였다.


import pygame, sys
# pygame.locals안의 상수들을 워낙 많이 사용해서 import를 이렇게 한다.
from pygame.locals import *

# pygame 초기화
pygame.init()
# pygame.display.set_mode는 윈도우에 대한 pygame.Surface 객체를 반환한다. 한 쌍의 값은 각각 너비, 높이이다.
# pygame.display.set_mode는 pygame.Surface 개체(Surface객체)를 반환해주고 변수에 저장한다.
DISPLAYSURF = pygame.display.set_mode((400,300))
# 캡션지정
pygame.display.set_caption('Hello World!')

# main game loop
# main loop는 3가지 일을 수행한다. 1. 이벤트 핸들링, 2. 게임상태 업데이트, 3. 게임 스테이트를 화면상에 그린다.
# 게임스테이트는 게임 프로그램 안에서 아용하는 모든 변수의 값을 통친한다. 게임 플레이어의 상태정보, 위치, 적의 상태, 위치등을 포함하며,
# 점수 환산이나, 누구의 차례인지 결정할 때 사용한다.
# 플레이어가 피해를 입거나, 적의 위치가 변경되거나 해서 특정 이벤트가 발생하면 게임 스테이트가 바뀌었다고 말한다.
# 지금까지 한 내용을 저장하는 것이 게임 스테이트를 저장하는 것이다.
# 게임 스테이트는 이벤트가 발생 or 시간이 지나면 바뀌게 된다.
# 게임루프: 이벤트 검사->게임 스테이트 업데이트(이벤트 핸들링)->새로운 스크린을 그린다.
# pygame에서는 pygame.event.get()에 의해서 새로 발생한 이벤트를 검사한다.
while True:
    for event in pygame.event.get():
        # pygame은 pygeame.event.Event객체(Event객체)에 이벤트를 기록한다.
        # pygame.event.get()을 호출하면 Event 객체의 list를 반환한다.
        # Event 객체의 list는 pygame.event.get()이 호출된 이후 발생한 이벤트이다.
        if event.type == QUIT:
            # Event 객체는 type이라는 멤버 변수(member variable)가 있고, 이를 통해 Event 객체의 종류를 알 수 있다.
            # event.type이 pygame.locals.QUIT라는 변수와 같은지 확인한다. import때문에 QUIT라고 사용할 수 있다.
            # pygame.locals에는 발생할 수 있는 이벤트의 type이 정의되어있다.
            pygame.quit()
            # pygame의 종료, 일반적으로 종료되면 pygame라이브러리가 종료되지만 가끔 오류가 있을 수 있어 명시적으로 종료한다.
            sys.exit()
            # python종료
        pygame.display.update()
