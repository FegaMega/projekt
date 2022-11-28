import pygame
import sys
from pygame.locals import * 
from player import Player
from Object import objects
from utils import checkCollisions
from coins import coin
sx = 700
sy = 700
screen = pygame.display.set_mode((sx, sy), 0, 32)
scroll = [0,0]
pygame.init()
FONT = pygame.font.SysFont("Helvetica-bold", 50)

coins = [coin(100, 600), coin(500, 400), coin(-41, sy - 50)]
Objects = [objects(50,600,50,50, (0,0,0), True), objects(500, 650, 50, 50, (255,255,255), True), objects(475, 600, 100, 50, (255,0,0), True), objects(900, 500, 50, 200, (0, 0, 0), True), objects(1000, 650, 300, 50, (0, 0, 0), False), objects(1000, 600, 300, 50, (0, 0, 0), True)]
player = Player()
collision_tolerance = 3
coinscollected = 0
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
            if event.key == K_w and player.jumps > 0 or event.key == K_UP and player.jumps > 0:
                player.mu = True
                player.jumps -= 1
        if event.type == pygame.KEYUP:
            if event.key == K_a or event.key == K_LEFT:
                player.ml = False
            if event.key == K_d or event.key == K_RIGHT:
                player.mr = False


    scroll[0] += (player.x-scroll[0] - sy/2)/10
    scroll[1] += (player.y-scroll[1] - sy/2)/10
    if scroll[1] > 0:
        scroll[1] = 0

    for ii in range (10):
        player.movement()
        player.y += player.yspeed
        if player.y >= sy - 50:
            player.y = sy - 50
            player.jumps = player.max_jumps
        else:
            player.yspeed += 0.4/60
        for Object in Objects:
            if Object.col == True:
                if checkCollisions(Object.x, Object.y, Object.xsize, Object.ysize, player.x, player.y, player.xsize, player.ysize):
                    player_bottom = player.y  + player.ysize
                    player_right = player.x + player.xsize
                    object_bottom = Object.y + Object.ysize
                    object_right = Object.x + Object.xsize
                    if abs(Object.y - player_bottom) < collision_tolerance:
                        player.y = Object.y - player.ysize
                        if player.yspeed >= 0:
                            player.yspeed = 0
                            player.jumps = player.max_jumps
                    elif abs(object_bottom - player.y) < collision_tolerance:
                        player.y = Object.y + Object.ysize
                        if player.yspeed < 0:
                            player.yspeed = 0
                    elif abs(object_right - player.x) < collision_tolerance:
                        if player.xspeed < 0:
                            player.x = object_right
                            player.xspeed = 0
                    elif abs(Object.x - player_right) < collision_tolerance:
                        if player.xspeed > 0:
                            player.x = Object.x - player.ysize
                            player.xspeed = 0
            
    for Coin in coins:
        if Coin.render == True:
            if checkCollisions(Coin.x, Coin.y, Coin.xsize, Coin.ysize, player.x, player.y, player.xsize, player.ysize):
                coinscollected += 1
                coins.remove(Coin)
                player.max_jumps += 1
        Coin.draw(scroll[0], scroll[1])
    player.draw(scroll[0], scroll[1])
    for Object in Objects:
        Object.draw(scroll[0], scroll[1])
    jumps_left = FONT.render(("jumps: " + str(player.jumps)), 1, (0, 0, 0))
    screen.blit(jumps_left, (10, 10))
    coinscollecteddraw = FONT.render(("coins: " + str(coinscollected)), 1, (0, 0, 0))
    screen.blit(coinscollecteddraw, (10, 50))
    pygame.display.update()
    pygame.time.Clock().tick(60)
    player.mu = False
