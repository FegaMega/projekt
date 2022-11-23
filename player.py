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
        self.xsize = 0
        self.ysize = 0
        self.xspeed = 0
        self.yspeed = 0 
        self.ml = False
        self.mr = False
        self.mu = False
        self.cj = False
        self.playe = pygame.Rect(self.x, self.y, 50, 50)
    
    def draw(self):
        playe = pygame.Rect(self.x, self.y, 50, 50)
        pygame.draw.rect(screen, (0, 0, 0), playe)
    def movement(self):
        if self.ml:
            self.x -= 3
        if self.mr:
            self.x += 3
        if self.mu and self.cj:
            self.yspeed = 9
        self.x = self.x + self.xspeed
        self.y = self.y + self.yspeed
