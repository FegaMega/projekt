import pygame
import sys
from pygame.locals import * 

screen = pygame.display.set_mode((800, 800), 0, 32)

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            pygame.quit()
    print('hello')
    pygame.display.update()