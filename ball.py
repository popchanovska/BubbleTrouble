import pygame
from settings import *

class Ball:
    def __init__(self, x, y, size, speed, direction):
        self.x = x
        self.y = y
        self.size = size
        self.speed_x, self.speed_y = speed
        self.direction = direction
        self.image = pygame.image.load("images/ball.png")
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * size / 3), int(self.image.get_height() * size / 3)))
        self.max_height = WINDOWHEIGHT / size

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x <= 0 or self.x >= WINDOWWIDTH - self.image.get_width():
            self.speed_x = -self.speed_x
        if self.y <= self.max_height or self.y >= WINDOWHEIGHT - self.image.get_height():
            self.speed_y = -self.speed_y


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
            if self.x <= 0:
                self.direction = DOWNRIGHT
            if self.y >= WINDOWHEIGHT - self.image.get_height():
                self.direction = UPLEFT

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
                self.direction = UPRIGHT
            if self.y <= self.max_height:
                self.direction = DOWNLEFT
