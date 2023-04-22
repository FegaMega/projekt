import pygame, time
from pygame.locals import * 
from player import Player
from Object import objects
from utils import checkCollisions, rot_center
from Extra_jump import extra_jump
from tunnels import tunnel
from portals import portal
from pistol import Pistol
from bullet import bullet
import json_levels
sx = 700
sy = 700
screen = pygame.display.set_mode((sx, sy), 0, 32)
scroll = [0,0]
TPallow: bool = True
pygame.init()
FONT = pygame.font.SysFont("Helvetica-bold", 50)
player = Player()
level = [[250.0, 650.0, 50, 50, [194, 60, 60], "object"], [650.0, 650.0, 50, 50, [0, 0, 0], "object"]]
nlev = ""
lev = []
i = 0


extra_jumps = [
    extra_jump(100, 600), 
    extra_jump(500, 300), 
    extra_jump(-41, sy - 50)
]
Objects = [
    
]
tunnels = [
    tunnel(1000, 650, 300, 50, (255, 0, 0))
]
portals = [
    portal(350, 650, 1400, 650)
]
gun = (  
    Pistol(player.x, player.y, 90)
)
bullets = [
    
]
for n in level:
    lev = level[i]
    if lev[len(lev) - 1] == "object":
        del(lev[len(lev) - 1])
    Objects.append(objects(lev[0], lev[1], lev[2], lev[3], lev[4]))
    i += 1
i = 0

now = pygame.time.Clock().get_time
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
            if event.key == K_LEFT:
                player.ml = True
            if event.key == K_RIGHT:
                player.mr = True
            if event.key == K_UP and player.jumps > 0 and player.in_tunnel == False:
                player.mu = True
                player.jumps -= 1
            if event.key == K_a:
                gun.change_angle = 10
            if event.key == K_d:
                gun.change_angle = -10
            if event.key == K_SPACE:
                bullets.append(bullet(gun.x, gun.y + 3, 3, gun.angle))
        if event.type == pygame.KEYUP:
            if event.key == K_LEFT:
                player.ml = False
            if event.key == K_RIGHT:
                player.mr = False
            if event.key == K_a:
                gun.rotleft = False
            if event.key == K_d:
                gun.rotleft = False
            if event.key == K_d:
                gun.change_angle = 0
            if event.key == K_a:
                gun.change_angle = 0
            
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
        for portal in portals:
            if checkCollisions(portal.xB, portal.yB, portal.xsizeB, portal.ysizeB, player.x, player.y, player.xsize, player.ysize) and TPallow == True:
                player.x = portal.xR
                player.y = portal.yR
                TPallow = False
                print('tp')
            if checkCollisions(portal.xR, portal.yR, portal.xsizeR, portal.ysizeR, player.x, player.y, player.xsize, player.ysize) and TPallow == True:
                player.x = portal.xB
                player.y = portal.yB
                TPallow = False
            if checkCollisions(portal.xR, portal.yR, portal.xsizeR, portal.ysizeR, player.x, player.y, player.xsize, player.ysize) == False and checkCollisions(portal.xB, portal.yB, portal.xsizeB, portal.ysizeB, player.x, player.y, player.xsize, player.ysize) == False:
                TPallow = True
            portal.draw(scroll[0], scroll[1])
    if gun.rotateleft == True:
        gun.angle -= 2
    if gun.rotateright == True:
        gun.angle += 2


    gun.rot()
    gun.x = player.x + 10
    gun.y = player.y + 20
    for Extra_jump in extra_jumps:
        if Extra_jump.render == True:
            if checkCollisions(Extra_jump.x, Extra_jump.y, Extra_jump.xsize, Extra_jump.ysize, player.x, player.y, player.xsize, player.ysize):
                extra_jumps.remove(Extra_jump)
                player.max_jumps += 1
        Extra_jump.draw(scroll[0], scroll[1])
    player.draw(scroll[0], scroll[1])
    for Bullet in bullets:
        Bullet.move()
        for portal in portals:
            if checkCollisions(portal.xR, portal.yR, portal.xsizeR, portal.ysizeR, Bullet.x, Bullet.y, Bullet.xsize, Bullet.ysize):
                bullets.remove(Bullet)
        for tunnel in tunnels:
            if checkCollisions(tunnel.x, tunnel.y, tunnel.xsize, tunnel.ysize, Bullet.x, Bullet.y, Bullet.xsize, Bullet.ysize):
                bullets.remove(Bullet)
        for Object in Objects:
            if checkCollisions(Object.x, Object.y, Object.xsize, Object.ysize, Bullet.x, Bullet.y, Bullet.xsize, Bullet.ysize):
                bullets.remove(Bullet)
        Bullet.draw(screen, scroll[0], scroll[1])
        if Bullet.frames_drawn > 500:
            bullets.remove(Bullet)
        Bullet.frames_drawn += 1
    gun.draw(scroll[0], scroll[1], screen)
    for Object in Objects:
        Object.draw(scroll[0], scroll[1])
    for tunnel in tunnels:
        tunnel.draw(scroll[0], scroll[1])
    

    jumps_left = FONT.render(("jumps: " + str(player.jumps)), 1, (0, 0, 0))
    screen.blit(jumps_left, (10, 10))
    pygame.display.update()
    pygame.time.Clock().tick(60)
    player.mu = False