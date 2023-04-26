import pygame
from pygame.locals import *

from utils import screen, sx, sy

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
        self.jumps = 0
        self.TPallow: bool = True
        self.on_floor: bool = False
        self.max_jumps = 1
        self.in_tunnel = False
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
        self.bottom:float = self.y + self.ysize
        self.right: float = self.x + self.xsize 
        self.collision_lines = [[self.right - 5, self.y + 5, 10, 1, "right"], [self.x - 5, self.bottom - 5, 10, 1, "left"], [self.x + 5, self.bottom - 5, 1, 10, "down"], [self.right - 5, self.bottom - 5, 1, 10, "down"], [self.right - 5, self.bottom - 5, 10, 1, "right"], [self.x - 5, self.y + 5, 10, 1, "left"], [self.x + 5, self.y - 5, 1, 10, "up"], [self.right - 5, self.y - 5, 1, 10, "up"]]