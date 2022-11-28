import pygame
import sys
from pygame.locals import * 
from player import Player
from Object import objects
from utils import checkCollisions
from Extra_jump import extra_jump
from tunnels import tunnel
sx = 700
sy = 700
screen = pygame.display.set_mode((sx, sy), 0, 32)
scroll = [0,0]
pygame.init()
FONT = pygame.font.SysFont("Helvetica-bold", 50)

extra_jumps = [
    extra_jump(100, 600), 
    extra_jump(500, 400), 
    extra_jump(-41, sy - 50)
]
Objects = [
    objects(50,600,50,50, (0,0,0)), 
    objects(500, 650, 50, 50, (255,255,255)), 
    objects(475, 600, 100, 50, (255,0,0)), 
    objects(900, 500, 50, 200, (0, 0, 0)), 
]
tunnels = [
    tunnel(1000, 650, 300, 50, (255, 0, 0))
]
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
            if event.key == K_w and player.jumps > 0 and player.in_tunnel == False or event.key == K_UP and player.jumps > 0 and player.in_tunnel == False:
                player.mu = True
                player.jumps -= 1
        if event.type == pygame.KEYUP:
            if event.key == K_a or event.key == K_LEFT:
                player.ml = False
            if event.key == K_d or event.key == K_RIGHT:
                player.mr = False
    player.in_tunnel = False


    scroll[0] += (player.x-scroll[0] - sy/2)/10
    scroll[1] += (player.y-scroll[1] - sy/2)/10
    if scroll[1] > 0:
        scroll[1] = 0

    for i in range(10):
        player.movement()
        player.y += player.yspeed
        if player.y >= sy - 50:
            player.y = sy - 50
            player.jumps = player.max_jumps
        else:
            player.yspeed += 0.4/60
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
                        player.jumps = player.max_jumps
                elif abs(object_bottom - player.y) < collision_tolerance:
                    player.y = object_bottom
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
    
        for tunnel in tunnels:
            if checkCollisions(tunnel.x, tunnel.y, tunnel.xsize, tunnel.ysize, player.x, player.y, player.xsize, player.ysize):
                player.in_tunnel = True
                player_bottom = player.y  + player.ysize
                tunnel_bottom = tunnel.y + tunnel.ysize
                if abs(tunnel.y - player_bottom) < collision_tolerance:
                    player.y = tunnel.y - player.ysize
                    if player.yspeed >= 0:
                        player.yspeed = 0
                        player.jumps = player.max_jumps
                    player.in_tunnel = False
                elif abs(tunnel_bottom - player.y) < collision_tolerance:
                    player.y = tunnel.y + tunnel.ysize
                    if player.yspeed < 0:
                        player.yspeed = 0
                    player.in_tunnel = False

    for Extra_jump in extra_jumps:
        if Extra_jump.render == True:
            if checkCollisions(Extra_jump.x, Extra_jump.y, Extra_jump.xsize, Extra_jump.ysize, player.x, player.y, player.xsize, player.ysize):
                extra_jumps.remove(Extra_jump)
                player.max_jumps += 1
        Extra_jump.draw(scroll[0], scroll[1])
    player.draw(scroll[0], scroll[1])
    for Object in Objects:
        Object.draw(scroll[0], scroll[1])
    for tunnel in tunnels:
        tunnel.draw(scroll[0], scroll[1])
    jumps_left = FONT.render(("jumps: " + str(player.jumps)), 1, (0, 0, 0))
    screen.blit(jumps_left, (10, 10))
    pygame.display.update()
    pygame.time.Clock().tick(60)
    player.mu = False
