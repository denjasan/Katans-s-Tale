import os
import pygame
from Constants import *
from groups import *

size = width, height = 800, 600


class Heart(pygame.sprite.Sprite):
    def __init__(self, group, image):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
        super().__init__(group)
        self.image = image
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = width // 2
        self.rect.y = height // 2

    def update(self, x, y):
        if self.rect.x == 0 and x > 0 or self.rect.x == width and x < 0:
            self.rect.x += x

        if self.rect.y == 0 and y > 0 or self.rect.y == height and y < 0:
            self.rect.y += y
