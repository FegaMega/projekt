import pygame


screen = pygame.display.set_mode((700, 700), 0, 32)

class extra_jump:
    def __init__(self, x, y, extra_info=[]):
        self.extra_info = extra_info
        self.x = x
        self.y = y
        self.xsize = 50
        self.ysize = 50
        self.rect = pygame.Rect(self.x, self.y, self.xsize, self.ysize)
        self.render: bool = True
        self.coinscollected = 0
    def draw(self, scroll_x, scroll_y):
        if self.render:
            self.rect = pygame.Rect(self.x - scroll_x, self.y - scroll_y, self.xsize, self.ysize)
            exjimg = pygame.image.load('power_up2.png').convert_alpha()
            screen.blit(exjimg, (self.x - scroll_x, self.y - scroll_y))
                