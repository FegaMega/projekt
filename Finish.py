import pygame
from utils import screen, sx, sy

class finish:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xsize = 50
        self.ysize = 50
        self.color = (50, 255, 0)
        self.rect = pygame.Rect(self.x, self.y, self.xsize, self.ysize)
    def draw(self, scroll_x, scroll_y):
        self.rect = pygame.Rect(self.x - scroll_x, self.y - scroll_y, self.xsize, self.ysize)
        pygame.draw.rect(screen, self.color, self.rect)