import pygame
import sys
from pygame.locals import * 
import player
from player import Player
import Object
from Object import objects
import utils
from utils import checkCollisions
sx = 800
sy = 800
screen = pygame.display.set_mode((sx, sy), 0, 32)

Objects = [objects(50,700,50,50, (0,0,0)), objects(500, 750, 50, 50, (255,255,255)), objects(475, 700, 100, 50, (255,0,0))]
player = Player()
collision_tolerance = 10
i = 0
r = True
while r:
    screen.fill((146,244,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            r = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                player.ml = True
            if event.key == K_d or event.key == K_RIGHT:
                player.mr = True
            if event.key == K_w and player.cj > 0 or event.key == K_UP and player.cj > 0:
                player.mu = True
                player.cj -= 1
        if event.type == pygame.KEYUP:
            if event.key == K_a or event.key == K_LEFT:
                player.ml = False
            if event.key == K_d or event.key == K_RIGHT:
                player.mr = False




    for ii in range (10):
        player.movement()
        player.y += player.yspeed
        if player.y >= 750:
            player.y = 750
            player.cj = 2
        else:
            player.yspeed += 0.4/45
        for Object in Objects:
            if checkCollisions(Object.x, Object.y, Object.xsize, Object.ysize, player.x, player.y, player.xsize, player.ysize):
                player_bottom = player.y  + player.ysize
                player_right = player.x + player.xsize
                object_bottom = Object.y + Object.ysize
                object_right = Object.x + Object.xsize
                if abs(Object.y - player_bottom) < collision_tolerance:
                    player.y = Object.y - player.ysize
                    if player.yspeed >= 0:
                        player.yspeed = 0
                        player.cj = 2
                if abs(object_bottom - player.y) < collision_tolerance:
                    player.y = Object.y + Object.ysize
                    if player.yspeed < 0:
                        player.yspeed = 0
                if abs(object_right - player.x) < collision_tolerance:
                    if player.xspeed < 0:
                        player.x = object_right
                if abs(Object.x - player_right) < collision_tolerance:
                    if player.xspeed > 0:
                        player.x = Object.x - player.ysize
            if player.x >= sx/2:
                player.x = sx/2
                Object.x -= player.yspeed
            elif player.x <= 200:
                player.x = 200
                Object.x -= player.xspeed
            Object.draw()
    i = 0
    ii = 0
    player.draw()
    pygame.display.update()
    pygame.time.Clock().tick(60)
    player.mu = False
