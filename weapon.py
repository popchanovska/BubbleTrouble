import pygame
from settings import *


class Weapon:
    def __init__(self, x=0, y=0):
        # self.type = type
        self.is_active = False
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/arrow.png")
        # self.rect = self.image.get_rect()

    def update(self):
        if self.is_active:
            if self.y <= 0:
                self.is_active = False
            else:
                self.y -= WEAPONSPEED
