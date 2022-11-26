import pygame
from pygame.locals import *

screen = pygame.display.set_mode((700, 700), 0, 32)

class objekts:
    def __init__(self):
        self.x = [400, 425, 200, 375]
        self.y = [650, 600, 650, 600]
        self.xsize = [50, 50, 50, 50]
        self.ysize = [50, 50, 50, 50]
        self.n = 4
        self.i = 0
        self.objekt = [pygame.Rect(self.x[self.i], self.y[self.i], self.xsize[self.i], self.ysize[self.i]), pygame.Rect(self.x[self.i], self.y[self.i], self.xsize[self.i], self.ysize[self.i]), pygame.Rect(self.x[self.i], self.y[self.i], self.xsize[self.i], self.ysize[self.i]), pygame.Rect(self.x[self.i], self.y[self.i], self.xsize[self.i], self.ysize[self.i])]
        self.color = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
    def draw(self):
        while self.i < self.n:
            self.objekt[self.i] = pygame.Rect(self.x[self.i], self.y[self.i], self.xsize[self.i], self.ysize[self.i])
            pygame.draw.rect(screen, self.color[self.i], self.objekt[self.i])
            self.i += 1
        self.i = 0
