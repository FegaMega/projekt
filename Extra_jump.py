import pygame


from utils import screen

class extra_jump:
    def __init__(self, x, y, extra_info=[]):
        self.extra_info = extra_info
        self.x = x
        self.y = y
        self.xsize = 50
        self.ysize = 50
        self.rect = pygame.Rect(self.x, self.y, self.xsize, self.ysize)
        self.coinscollected = 0
    def draw(self, scroll_x, scroll_y):
        self.rect = pygame.Rect(self.x - scroll_x, self.y - scroll_y, self.xsize, self.ysize)
        exjimg = pygame.image.load('power_up2.png').convert_alpha()
        screen.blit(exjimg, (self.x - scroll_x, self.y - scroll_y))
                