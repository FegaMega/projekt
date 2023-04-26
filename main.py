import pygame, time
from pygame.locals import * 
from player import Player
from Object import objects
from utils import checkCollisions, rot_center, screen, sx, sy
from Extra_jump import extra_jump
from tunnels import tunnel
from portals import portal
from pistol import Pistol
from bullet import bullet
import json_levels

pygame.init()

# Fixar saker
scroll = [0,0]
TPallow: bool = True
FONT = pygame.font.SysFont("Helvetica-bold", 50)
player = Player()
json_level = [[250.0, 650.0, 50, 50, [194, 60, 60], "object"], [650.0, 650.0, 50, 50, [0, 0, 0], "object"]]
nlev = ""
lev = []
i = 0
collision_tolerance = 3
coinscollected = 0
i = 0
ObjectsNotTouched = 0


extra_jumps = [
    extra_jump(100, 600), 
    extra_jump(500, 300), 
    extra_jump(-41, sy - 50)
]
Level = [
    
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
# Lägger in extra_jumps, tunnel, json_level och portal i Level
for ExtraJumps in extra_jumps:
    Level.append(extra_jump(ExtraJumps.x, ExtraJumps.y, "ExtraJumps"))
for Tunnel in tunnels:
    Level.append(tunnel(Tunnel.x, Tunnel.y, Tunnel.xsize, Tunnel.ysize, Tunnel.color, "Tunnel"))
for Portal in portals:
    Level.append(portal(Portal.xB, Portal.yB, Portal.xR, Portal.yR, "Portal"))
for n in json_level:
    lev = json_level[i]
    if lev[len(lev) - 1] == "object":
        del(lev[len(lev) - 1])
    Level.append(objects(lev[0], lev[1], lev[2], lev[3], lev[4]))
    i += 1
i = 0

#klockan
now = pygame.time.Clock().get_time

#spel loopen
r = True
while r:
    screen.fill((146,244,255))
    for event in pygame.event.get():
        #Quit kod
        if event.type == QUIT:
            r = False
        #inputs

        #ON
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
        #OFF
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
            


    #Scroll effekt 
    scroll[0] += (player.x-scroll[0] - sy/2)/10
    scroll[1] += (player.y-scroll[1] - sy/2)/10
    if scroll[1] > 0:
        scroll[1] = 0
    
    #sätter player.in_tunnel av för collision loopen
    player.in_tunnel = False
    
    #collision loopen
    for i in range(10):
        #sätter N till 0 så att den kan räkna mängden gånger den har gått igenom objekt collsion loopen
        n = 0
        #Rör spelaren
        player.movement()
        #säger att spelaren inte är på golvet
        player.on_floor = False
        #kollar om spelaren är under kamerans botten
        if player.y >= sy - player.ysize:
            player.y = sy - player.ysize
            player.on_floor = True
        else:
        #Gravitation
            player.yspeed += 0.4/60
        #objekt collision loopen
        for object in Level:
            #kollar om det är en portal (de är speciella)
            if object.__class__ == portal:
                if checkCollisions(object.xR, object.yR, object.xsizeR, object.ysizeR, player.x, player.y, player.xsize, player.ysize) == True:
                    if TPallow == True:
                        player.x = object.xB
                        player.y = object.yB
                        TPallow = False
                elif checkCollisions(object.xB, object.yB, object.xsizeB, object.ysizeB, player.x, player.y, player.xsize, player.ysize) == True:
                    if TPallow == True:
                        player.x = object.xR
                        player.y = object.yR
                        TPallow = False
                else:
                    TPallow = True
            #vanliga objekts kod
            else:
                #Kollar om spelaren är inuti objektet
                if checkCollisions(object.x, object.y, object.xsize, object.ysize, player.x, player.y, player.xsize, player.ysize) == True:
                    #Kollar om det är en extra_jump
                    if object.__class__ == extra_jump:
                        player.max_jumps += 1
                        #tar bort extra_jump saken
                        Level.pop(n)
                    else:
                        #Kollar vilken sida som nuddade objektet med linjer på spelaren  
                        for line in player.collision_lines:
                            if checkCollisions(line[0], line[1], line[2], line[3], object.x, object.y, object.xsize, object.ysize) == True:
                                #vanliga objekt
                                if object.__class__ != tunnel:
                                    player.in_tunnel = False
                                    if line[4] == "right":
                                        player.x = object.x - player.xsize
                                        player.xspeed = 0
                                    elif line[4] == "left":
                                        player.x = object.x + object.xsize
                                        player.xspeed = 0
                                    elif line[4] == "down":
                                        player.y = object.y - player.ysize
                                        player.yspeed = 0
                                        player.on_floor = True
                                    elif line[4] == "up":
                                        player.y = object.y + object.ysize
                                        player.yspeed = 0
                                #tunnlar
                                else:
                                #Kollar ifall spelaren är på/under tunneln eller om den är i 
                                    if line[4] == "right" or line[4] == "left":
                                        player.in_tunnel = True
                                    if player.in_tunnel == False:
                                        if line[4] == "down":
                                            player.y = object.y - player.ysize
                                            player.yspeed = 0
                                            player.on_floor = True
                                        elif line[4] == "up":
                                            player.y = object.y + object.ysize
                                            player.yspeed = 0
            #lägger till ett så att jag vet att jag är i nästa objekt i listan Level
            n += 1
        #resetar mina hopp ifall jag är på marken
        if player.on_floor == True:
            player.jumps = player.max_jumps


    #Roterar vapnbet
    if gun.rotateleft == True:
        gun.angle -= 2
    if gun.rotateright == True:
        gun.angle += 2
    gun.rot()
    #flyttar vapnet till spelaren
    gun.x = player.x + 10
    gun.y = player.y + 20

    #ritar spelaren
    player.draw(scroll[0], scroll[1])
    #Kollar om skotten rör vid ett objekt och flyttar de fram
    for Bullet in bullets:
        Bullet.move()
        for Object in Level:
            if Object.__class__ == portal:
                if checkCollisions(Object.xB, Object.yB, Object.xsizeB, Object.ysizeB, Bullet.x, Bullet.y, Bullet.xsize, Bullet.ysize) == True or checkCollisions(Object.xR, Object.yR, Object.xsizeR, Object.ysizeR, Bullet.x, Bullet.y, Bullet.xsize, Bullet.ysize) == True:
                    bullets.remove(Bullet)
            else:
                if checkCollisions(Object.x, Object.y, Object.xsize, Object.ysize, Bullet.x, Bullet.y, Bullet.xsize, Bullet.ysize):
                    bullets.remove(Bullet)
        Bullet.draw(screen, scroll[0], scroll[1])
        #kollar om skotten är gamla
        if Bullet.frames_drawn > 500:
            bullets.remove(Bullet)
        Bullet.frames_drawn += 1
    #Ritar vapnet
    gun.draw(scroll[0], scroll[1], screen)
    #Ritar objekten i Level
    for Object in Level:
        Object.draw(scroll[0], scroll[1])
    #ritat kollision linjerna på spelar(tillfällig)
    for i in player.collision_lines:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(i[0] - scroll[0], i[1] - scroll[1], i[2], i[3]))
    
    #Skriver hur många hopp spelaren har kvar på skärmen
    jumps_left = FONT.render(("jumps: " + str(player.jumps) + "/" + str(player.max_jumps)), 1, (0, 0, 0))
    screen.blit(jumps_left, (10, 10))
    #uppdaterar skärmen
    pygame.display.update()
    #60 Fps limmit
    pygame.time.Clock().tick(60)
    #spelaren rör sig inte upp 
    player.mu = False

