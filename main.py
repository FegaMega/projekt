import pygame
import sys
from pygame.locals import * 
import player
from player import Player
import Object
from Object import objects


screen = pygame.display.set_mode((700, 700), 0, 32)

Objects = [objects(50,700,50,50, (0,0,0)), objects(500, 750, 50, 50, (0,0,0)), objects(475, 700, 100, 50, (0,0,0))]
player = Player()
collision_tolerance = 20
i = 0

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
                player.cj -= 1
        if event.type == pygame.KEYUP:
            if event.key == K_a or event.key == K_LEFT:
                player.ml = False
            if event.key == K_d or event.key == K_RIGHT:
                player.mr = False


    player.movement()
    player.y += player.yspeed
    if player.y >= 650:
        player.y = 650
        player.cj = True
    else:
        player.yspeed += 0.4

    while i < 4:
        player.movement()
        for objecT in Objects:
            playe = pygame.Rect(player.x, player.y, 50, 50)
            objects = pygame.Rect(objects.x, objects.y, objects.xsize, objects.ysize)
            if pygame.Rect.colliderect(playe, objects):
                player_bottom = player.y  + player.ysize
                player_right = player.x + player.xsize
                object_bottom = objects.y + objects.ysize
                object_right = objects.x + objects.xsize
                if abs(objects.y - player_bottom) < collision_tolerance:
                    player.y = objects.y - player.ysize
                    if player.yspeed >= 0:
                        player.yspeed = 0
                        player.cj = True
                        print('bottom')
                if abs(object_bottom - player.y) < collision_tolerance:
                    player.y = objects.y + objects.ysize
                    if player.yspeed < 0:
                        player.yspeed = 0
                        print('top')
                if abs(object_right - player.x) < collision_tolerance:
                    player.x = object_right
                    print('left')
                if abs(objects.x - player_right) < collision_tolerance:
                    player.x = objects.x - player.ysize
                    print('right')
            objects.i += 1
        i += 1
    objects.i = 0
    i = 0
    objects.draw()
    player.draw()
    pygame.display.update()
    pygame.time.Clock().tick(60)
    player.mu = False
