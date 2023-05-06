import pygame, math
from datetime import datetime, timedelta

class bullet:
    def __init__(self, x, y, speed, angle):
        self.x = x
        self.y = y
        self.speed: float = speed
        self.angle: float = angle
        self.xsize = 6
        self.ysize = 3
        self.frames_drawn = 0
        self.og_surf = pygame.transform.smoothscale(pygame.image.load("bullet.png").convert_alpha(), (self.xsize, self.ysize))
        self.surf = pygame.transform.rotate(self.og_surf, self.angle)
        self.rect = pygame.Rect(self.x, self.y, self.xsize, self.ysize)
        self.TPallow: bool = True
    def move(self):
        self.x += (math.cos(math.radians(self.angle))) * self.speed
        self.y -= (math.sin(math.radians(self.angle))) * self.speed
    def draw(self, screen, scroll_x, scroll_y):
        self.rect = pygame.Rect(self.x  - scroll_x, self.y - scroll_y, self.xsize, self.ysize)
        screen.blit(self.surf, (self.x - scroll_x, self.y - scroll_y))