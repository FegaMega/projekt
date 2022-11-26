import pygame
from pygame.locals import *

sx = 800
sy = 800
screen = pygame.display.set_mode((sx, sy), 0, 32)

class Player:
    def __init__(self):
        self.x = 250
        self.y = 650
        self.xsize = 50
        self.ysize = 50
        self.xspeed = 0
        self.yspeed = 0 
        self.ml: bool = False
        self.mr: bool = False
        self.mu: bool = False
        self.cj = 2
        self.xhitbox: bool = True
        self.yhitbox: bool = True
        self.playe = pygame.Rect(self.x, self.y, self.xsize, self.ysize)
    
    def draw(self, scrollx, scrolly):
        playe = pygame.Rect(self.x - scrollx, self.y - scrolly, 50, 50)
        pygame.draw.rect(screen, (0, 255, 0), playe)
    def movement(self):
        if self.ml:
            self.xspeed = -3/8
        if self.mr:
            self.xspeed = 3/8
        if self.mr == False and self.ml == False:           
            self.xspeed = 0
        if self.mu == True:
            self.yspeed = -9/11
        self.x += self.xspeed
        self.y += self.yspeed