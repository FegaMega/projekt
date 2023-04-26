import pygame
from utils import screen


class portal:
    def __init__(self, xB, yB, xR, yR, extra_info=[]):
        self.extra_info = extra_info
        self.xB = xB
        self.yB = yB
        self.xsizeB = 38
        self.ysizeB = 50
        self.rectB = pygame.Rect(self.xB, self.yB, self.xsizeB, self.ysizeB)
        self.xR = xR
        self.yR = yR
        self.xsizeR = 38
        self.ysizeR = 50
        self.rectB = pygame.Rect(self.xR, self.yR, self.xsizeR, self.ysizeR)
    def draw(self, scroll_x, scroll_y):
        self.rect = pygame.Rect(self.xR - scroll_x, self.yR - scroll_y, self.xsizeR, self.ysizeR)
        portalB = pygame.image.load('portal blue.png').convert_alpha()
        self.rect = pygame.Rect(self.xB - scroll_x, self.yB - scroll_y, self.xsizeB, self.ysizeB)
        portalR = pygame.image.load('portal red.png').convert_alpha()
        screen.blit(portalB, (self.xB - scroll_x, self.yB - scroll_y))
        screen.blit(portalR, (self.xR - scroll_x, self.yR - scroll_y))

