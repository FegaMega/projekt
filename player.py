import pygame
from pygame.locals import *

screen = pygame.display.set_mode((800, 800), 0, 32)

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.xspeed = 0
        self.yspeed = 0 
        self.ml = False
        self.mr = False
    def draw(self):
        if self.ml:
            self.x -= 3
        if self.mr:
            self.x += 3
        self.x = self.x + self.xspeed
        self.y = self.y + self.yspeed
        playe = pygame.Rect(self.x, self.y, 50, 50)
        pygame.draw.rect(screen, (0, 0, 0), playe)