import pygame
import sys
from pygame.locals import * 
import player
from player import Player
import objects
from objects import objekts

screen = pygame.display.set_mode((700, 700), 0, 32)

objects = objekts()
player = Player()


while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                player.ml = True
            if event.key == K_d or event.key == K_RIGHT:
                player.mr = True
            if event.key == K_w or event.key == K_UP:
                player.mu = True
        if event.type == pygame.KEYUP:
            if event.key == K_a or event.key == K_LEFT:
                player.ml = False
            if event.key == K_d or event.key == K_RIGHT:
                player.mr = False
            if event.key == K_w or event.key == K_UP:
                player.mu = False
    player.movement()
    while objects.i < objects.n:
        playe = pygame.Rect(player.x, player.y, 50, 50)
        objects.objekt[objects.i] = pygame.Rect(objects.x[objects.i], objects.y[objects.i], objects.sizex[objects.i], objects.y[objects.i])
        if pygame.Rect.colliderect(playe, objects.objekt[objects.i]):
            print('he')
            if player.x + 50 <= objects.x[objects.i] + 10:
                player.x = objects.x[objects.i] - player.xsize 
        objects.i += 1
    objects.i = 0
    objects.draw()
    player.draw()
    pygame.display.update()
    pygame.time.Clock().tick(60)