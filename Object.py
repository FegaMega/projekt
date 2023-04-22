import pygame

screen = pygame.display.set_mode((700, 700), 0, 32)

class objects:
    def __init__(self, x, y, xsize, ysize, color, extra_info=[]):
        self.extra_info = extra_info
        self.x = x
        self.y = y
        self.xsize = xsize
        self.ysize = ysize
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.xsize, self.ysize)
    def draw(self, scroll_x, scroll_y):
        self.rect = pygame.Rect(self.x - scroll_x, self.y - scroll_y, self.xsize, self.ysize)
        pygame.draw.rect(screen, self.color, self.rect)
                
