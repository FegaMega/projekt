import pygame
import sys
from pygame.locals import *
from player import Player
from Object import objects
from utils import checkCollisions, screen, sy
from Extra_jump import extra_jump
from tunnels import tunnel
from portals import portal
from pistol import Pistol
from bullet import bullet


# Fixar saker

class spel:
    def __init__(self):
        self.player = Player()
        self.extra_jumps = [
            extra_jump(100, 600),
            extra_jump(500, 300),
            extra_jump(-41, sy - 50)]
        self.Level = []
        self.tunnels = [
            tunnel(1000, 600, 300, 50, (255, 0, 0))]
        self.portals = [
            portal(350, 650, 1400, 650)]
        self.gun = (Pistol(self.player.x, self.player.y, 90))
        self.bullets = []
        self.scroll = [0, 0]
        self.TPallow: bool
        self.FONT = pygame.font.SysFont("Helvetica-bold", 50)
        self.json_level = [[250.0, 650.0, 50, 50, [194, 60, 60], "object"], [650.0, 650.0, 50, 50, [0, 0, 0], "object"]]
        self.nlev = ""
        self.lev = []
        self.collision_tolerance = 3
        self.coinscollected = 0
        self.ObjectsNotTouched = 0
        self.TPallow: bool = True
        for ExtraJumps in self.extra_jumps:
            self.Level.append(extra_jump(ExtraJumps.x, ExtraJumps.y, "ExtraJumps"))
        for Tunnel in self.tunnels:
            self.Level.append(tunnel(Tunnel.x, Tunnel.y, Tunnel.xsize, Tunnel.ysize, Tunnel.color, "Tunnel"))
        for Portal in self.portals:
            self.Level.append(portal(Portal.xB, Portal.yB, Portal.xR, Portal.yR, "Portal"))
        for n in self.json_level:
            if n[len(n) - 1] == "object":
                del (n[len(n) - 1])
            self.Level.append(objects(n[0], n[1], n[2], n[3], n[4]))

    def checkEvent(self, event):
        # ON
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                self.player.ml = True
            if event.key == K_RIGHT:
                self.player.mr = True
            if event.key == K_UP and self.player.jumps > 0 and False == self.player.in_tunnel:
                self.player.mu = True
                self.player.jumps -= 1
            if event.key == K_a:
                self.gun.change_angle = 10
            if event.key == K_d:
                self.gun.change_angle = -10
            if event.key == K_SPACE:
                self.bullets.append(bullet(self.gun.x, self.gun.y + 3, 3, self.gun.angle))
        # OFF
        if event.type == pygame.KEYUP:
            if event.key == K_LEFT:
                self.player.ml = False
            if event.key == K_RIGHT:
                self.player.mr = False
            if event.key == K_a:
                self.gun.rotleft = False
            if event.key == K_d:
                self.gun.rotleft = False
            if event.key == K_d:
                self.gun.change_angle = 0
            if event.key == K_a:
                self.gun.change_angle = 0


    def rullaBild(self):
        self.scroll[0] += (self.player.x - self.scroll[0] - sy / 2) / 10
        self.scroll[1] += (self.player.y - self.scroll[1] - sy / 2) / 10
        if self.scroll[1] > 0:
            self.scroll[1] = 0
    def golvCheck(self):
        # kollar om spelaren är under kamerans botten
        if self.player.y >= sy - self.player.ysize:
            self.player.y = sy - self.player.ysize
            self.player.on_floor = True
        else:
            # Gravitation
            # säger att spelaren inte är på golvet
            self.player.yspeed += 0.4 / 60
            self.player.on_floor = False

            
    def portalKollision(self,object):
        if checkCollisions(object.xR, object.yR, object.xsizeR, object.ysizeR, self.player.x, self.player.y, self.player.xsize, self.player.ysize):
            if self.TPallow == True:
                self.player.x = object.xB
                self.player.y = object.yB
                self.TPallow = False
        elif checkCollisions(object.xB, object.yB, object.xsizeB, object.ysizeB, self.player.x, self.player.y, self.player.xsize, self.player.ysize):
            if self.TPallow == True:
                self.player.x = object.xR
                self.player.y = object.yR
                self.TPallow = False
        else:
            self.TPallow = True
    def collektebleCheck(self, n):
        # Kollar om det är en extra_jump
        if object.__class__ == extra_jump:
            self.player.max_jumps += 1
            # tar bort extra_jump saken
            del self.Level[n]
    def TunnelKollision(self, line, object):
        # Kollar ifall spelaren är på/under tunneln eller om den är i
        if line[4] == "right" or line[4] == "left":
            self.player.in_tunnel = True
        if self.player.in_tunnel == False:
            if line[4] == "down":
                self.player.y = object.y - self.player.ysize
                self.player.yspeed = 0
                self.player.on_floor = True
            elif line[4] == "up":
                self.player.y = object.y + object.ysize
                self.player.yspeed = 0
    def vanligaObjektsKollision(self, line, object):
        self.player.in_tunnel = False
        if line[4] == "right":
            self.player.x = object.x - self.player.xsize
            self.player.xspeed = 0
        elif line[4] == "left":
            self.player.x = object.x + object.xsize
            self.player.xspeed = 0
        elif line[4] == "down":
            self.player.y = object.y - self.player.ysize
            self.player.yspeed = 0
            self.player.on_floor = True
        elif line[4] == "up":
            self.player.y = object.y + object.ysize
            self.player.yspeed = 0
    def linjeKollisiomMedObjekt(self, object):
        for line in self.player.collision_lines:
            if checkCollisions(line[0], line[1], line[2], line[3], object.x, object.y, object.xsize, object.ysize):
                # vanliga objekt
                if object.__class__ != tunnel:
                    self.vanligaObjektsKollision(line, object)
                else:
                    self.TunnelKollision(line, object)
    def kollision(self):
        for i in range(10):
            # sätter N till 0 så att den kan räkna mängden gånger den har gått igenom objekt collsion loopen
            n = 0
            # Rör spelaren
            self.player.movement()
            # kollar om spelaren är under kamerans botten
            self.golvCheck()
            # objekt collision loopen
            for object in self.Level:
                # kollar om det är en portal (de är speciella)
                if object.__class__ == portal:
                    self.portalKollision(object)
                # vanliga objekts kod
                else:
                    # Kollar om spelaren är inuti objektet
                    if checkCollisions(object.x, object.y, object.xsize, object.ysize, self.player.x, self.player.y, self.player.xsize, self.player.ysize):
                        # Kollar om det är en extra_jump
                        if object.__class__ == extra_jump:
                            self.player.max_jumps += 1
                            # tar bort extra_jump saken
                            del self.Level[n]
                        else:
                            # Kollar vilken sida som nuddade objektet med linjer på spelaren
                            self.linjeKollisiomMedObjekt(object)
                # lägger till ett så att jag vet att jag är i nästa objekt i listan mittSpel.Level
                n += 1
        # resetar mina hopp ifall jag är på marken
        if self.player.on_floor == True:
            self.player.jumps = self.player.max_jumps    
def main() -> int:
    pygame.init()
    mittSpel = spel()

    # spel loopen
    r = True
    while r:
        screen.fill((146, 244, 255))
        # Töm event kön
        for event in pygame.event.get():
            # Quit kod
            if event.type == QUIT:
                r = False
            # inputs
            mittSpel.checkEvent(event)

        # Scroll effekt
        mittSpel.rullaBild()

        # sätter player.in_tunnel av för collision loopen
        mittSpel.player.in_tunnel = False

        # collision loopen
        mittSpel.kollision()

        # Roterar vapnbet
        if mittSpel.gun.rotateleft == True:
            mittSpel.gun.angle -= 2
        if mittSpel.gun.rotateright == True:
            mittSpel.gun.angle += 2
        mittSpel.gun.rot()
        # flyttar vapnet till spelaren
        mittSpel.gun.x = mittSpel.player.x + 10
        mittSpel.gun.y = mittSpel.player.y + 20

        # ritar spelaren
        mittSpel.player.draw(mittSpel.scroll[0], mittSpel.scroll[1])
        # Kollar om skotten rör vid ett objekt och flyttar de fram
        for Bullet in mittSpel.bullets:
            Bullet.move()
            for Object in mittSpel.Level:
                if Object.__class__ == portal:
                    if checkCollisions(Object.xB,
                                               Object.yB,
                                               Object.xsizeB,
                                               Object.ysizeB,
                                               Bullet.x,
                                               Bullet.y,
                                               Bullet.xsize,
                                               Bullet.ysize) == True and True == checkCollisions(Object.xR, Object.yR,
                                                                                                 Object.xsizeR,
                                                                                                 Object.ysizeR, Bullet.x,
                                                                                                 Bullet.y,
                                                                                                 Bullet.xsize, Bullet.ysize):
                        continue
                    mittSpel.bullets.remove(Bullet)
                else:
                    if checkCollisions(Object.x, Object.y, Object.xsize, Object.ysize, Bullet.x, Bullet.y, Bullet.xsize,
                                       Bullet.ysize):
                        mittSpel.bullets.remove(Bullet)
            Bullet.draw(screen, mittSpel.scroll[0], mittSpel.scroll[1])
            # kollar om skotten är gamla
            if Bullet.frames_drawn > 500:
                mittSpel.bullets.remove(Bullet)
            Bullet.frames_drawn += 1
        # Ritar vapnet
        mittSpel.gun.draw(mittSpel.scroll[0], mittSpel.scroll[1], screen)
        # Ritar objekten i mittSpel.Level
        for Object in mittSpel.Level:
            Object.draw(mittSpel.scroll[0], mittSpel.scroll[1])
        # ritat kollision linjerna på spelar(tillfällig)
        for i in mittSpel.player.collision_lines:
            pygame.draw.rect(screen, (255, 0, 0),
                             pygame.Rect(i[0] - mittSpel.scroll[0], i[1] - mittSpel.scroll[1], i[2], i[3]))

        # Skriver hur många hopp spelaren har kvar på skärmen
        jumps_left = mittSpel.FONT.render(("jumps: " + str(mittSpel.player.jumps) + "/" + str(mittSpel.player.max_jumps)), True,
                                          (0, 0, 0))
        screen.blit(jumps_left, (10, 10))
        # uppdaterar skärmen
        pygame.display.update()
        # 60 Fps limmit
        pygame.time.Clock().tick(60)
        # spelaren rör sig inte upp
        mittSpel.player.mu = False
    return 0


if __name__ == '__main__':
    sys.exit(main())
