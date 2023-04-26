import pygame
from utils import rot_center, screen




class Pistol:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.xsize = 25
        self.ysize = 15
        self.angle = angle
        self.rect = pygame.Rect(self.x, self.y, self.xsize, self.ysize)
        self.rotateleft = False
        self.rotateright = False
        self.change_angle = 0
        self.og_surf = pygame.transform.smoothscale(pygame.image.load("gun.png").convert_alpha(), (self.xsize, self.ysize))
        self.surf = self.og_surf

    def rot(self):
        self.angle += self.change_angle
        self.angle = self.angle % 360
        self.rect = self.surf.get_rect(center=self.rect.center)
        self.surf = pygame.transform.rotate(self.og_surf, self.angle)
    def draw(self, scroll_x, scroll_y, screen):
        self.rect = pygame.Rect(self.x - scroll_x, self.y - scroll_y, self.xsize, self.ysize)
        screen.blit(self.surf, (self.x - scroll_x, self.y - scroll_y))



