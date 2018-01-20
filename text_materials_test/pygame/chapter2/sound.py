import pygame
import sys
import time
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Sound')

while True: # main game loop
    soundObj = pygame.mixer.Sound("beep1.ogg")
    soundObj.play()
    time.sleep(1)  # 1초 동안 소리를 재생하도록 둔다.
    soundObj.stop()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
