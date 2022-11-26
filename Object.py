import pygame
from pygame.locals import *

screen = pygame.display.set_mode((700, 700), 0, 32)

class objects:
    def __init__(self, x, y, xsize, ysize, color):
        self.x = x
        self.y = y
        self.xsize = xsize
        self.ysize = ysize
        self.color = color
    def draw(self):
        while self.i < self.n:
            self.rect = pygame.Rect(self.x, self.y, self.xsize, self.ysize, self.color)
            pygame.draw.rect(screen, self.color, self.rect)
            self.i += 1
        self.i = 0
