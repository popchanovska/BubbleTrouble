import pygame
from settings import *
from weapon import *
class Player:
    def __init__(self):
        self.x = WINDOWWIDTH / 2
        self.y = WINDOWHEIGHT - 40
        self.weapon = Weapon()
        self.image = pygame.image.load('images/player.png')
        self.moving_left = False
        self.moving_right = False
        # self.rect = self.image.get_rect()

    def shoot(self):
        self.weapon = Weapon(self.x + self.image.get_width()/2, self.y)
        self.weapon.is_active = True

    def update(self):
        if self.moving_left and self.x > 0:
            self.x -= PLAYERSPEED
        if self.moving_right and self.x < WINDOWWIDTH - self.image.get_width():
            self.x += PLAYERSPEED
        if self.weapon.is_active:
            self.weapon.update()
