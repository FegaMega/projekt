import pygame


screen = pygame.display.set_mode((800, 800), 0, 32)

class coin:
    def __init__(self, x, y, xsize, ysize):
        self.x = x
        self.y = y
        self.xsize = xsize
        self.ysize = ysize
        self.rect = pygame.Rect(self.x, self.y, self.xsize, self.ysize)
        self.render: bool = True
        self.coinscollected = 0
    def draw(self, scroll_x, scroll_y):
        if self.render:
            self.rect = pygame.Rect(self.x - scroll_x, self.y - scroll_y, self.xsize, self.ysize)
            coinimg = pygame.image.load('coin4.png').convert_alpha()
            screen.blit(coinimg, (self.x - scroll_x, self.y - scroll_y))
                