import pygame
from main import screen

class objekts:
    def __init__(self):
        self.x = [400]
        self.y = [750]
        self.sizex = [50]
        self.sizey = [50]
        self.n = 1
        self.i = 0
        self.objekt = [pygame.Rect(self.x[self.i], self.y[self.i], self.sizex[self.i], self.y[self.i])]
        self.color = [(0, 0, 0)]
    def draw(self):
        while self.i%self.n < self.n:
            self.objekt[self.i] = pygame.Rect(self.x[self.i], self.y[self.i], self.sizex[self.i], self.y[self.i])
            pygame.draw.rect(screen, self.color[self.i], self.objekt[self.i])
            i += 1
        i = 0
