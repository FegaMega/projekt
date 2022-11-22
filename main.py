import pygame
import sys
from pygame.locals import * 
import player
from player import Player

screen = pygame.display.set_mode((800, 800), 0, 32)

player = Player()

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            pygame.quit()
        
        if event.type == pygame.KEYUP:
            if event.key == K_a or event.key == K_LEFT:
                Player.ml = True
            if event.key == K_d or event.key == K_RIGHT:
                player.mr = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                player.ml = False
            if event.key == K_d or event.key == K_RIGHT:
                player.mr = False
    player.movement()
    player.draw()
    pygame.display.update()