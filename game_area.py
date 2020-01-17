import pygame

from groups import *
from Constants import *


class Area(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(areaG)
        self.image = pygame.image.load('data/fon/first_back.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.y = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.bottom = HEIGHT
        self.add(fon_group)


class AreaX(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(areaGX)
        self.image = pygame.image.load('data/fon/x1.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.y = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.bottom = HEIGHT
        self.add(fon_group)

