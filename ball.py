import pygame
from settings import *

class Ball:
    def __init__(self, x, y, size, direction):
        self.x = x
        self.y = y
        self.size = size
        self.direction = direction
        self.image = pygame.image.load("images/ball.png")
        self.max_height = WINDOWHEIGHT / size

    def update(self):
        if self.direction == DOWNRIGHT:
            self.x += 1 #odi desno
            self.y += 5 #odi gore
            if self.x >= WINDOWWIDTH - self.image.get_width():
                self.direction = DOWNLEFT #ako se cukni, menva nasoka
            if self.y >= WINDOWHEIGHT - self.image.get_height():
                self.direction = UPRIGHT

        if self.direction == DOWNLEFT:
            self.x -= 1
            self.y += 5
            if self.x >= WINDOWWIDTH - self.image.get_width():
                self.direction = DOWNLEFT
            if self.y >= WINDOWHEIGHT - self.image.get_height():
                self.direction = UPRIGHT

        if self.direction == UPRIGHT:
            self.x += 1
            self.y -= 5
            if self.x >= WINDOWWIDTH - self.image.get_width():
                self.direction = UPLEFT
            if self.y <= self.max_height:
                self.direction = DOWNRIGHT
        if self.direction == UPLEFT:
            self.x -= 1
            self.y -= 5
            if self.x <= 0:
                self.direction = DOWNRIGHT
            if self.y <= self.max_height:
                self.direction = DOWNLEFT