import pygame
from pygame.locals import *
import objects
from objects import objekts

objects = objekts()

screen = pygame.display.set_mode((700, 700), 0, 32)

class Player:
    def __init__(self):
        self.x = 0
        self.y = 650
        self.xsize = 50
        self.ysize = 50
        self.xspeed = 0
        self.yspeed = 0 
        self.ml: bool = False
        self.mr: bool = False
        self.mu: bool = False
        self.cj: bool = False
        self.xhitbox: bool = True
        self.yhitbox: bool = True
        self.playe = pygame.Rect(self.x, self.y, self.xsize, self.ysize)
    
    def draw(self):
        playe = pygame.Rect(self.x, self.y, 50, 50)
        pygame.draw.rect(screen, (0, 0, 0), playe)
    def movement(self):
        if self.ml:
            self.x -= 3
        if self.mr == True:
            self.x += 3
        if self.mu == True:
            self.yspeed = -7
        self.x += self.xspeed
        self.y += self.yspeed
