# encoding: utf-8
import pygame

from groups import *
from Constants import *


class AreaY1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(areaG)
        self.image = pygame.image.load('data/fon/y1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 117
        self.mask = pygame.mask.from_surface(self.image)
        self.bottom = HEIGHT
        self.add(all_sprites)
        self.add(fon_group)


class AreaX1(pygame.sprite.Sprite):
    def __init__(self, flag=False):
        super().__init__(areaGX)
        self.image = pygame.image.load('data/fon/x1.png')
        self.rect = self.image.get_rect()
        if not flag:
            self.rect.x = 0
        else:
            self.rect.x = -215
        self.rect.y = 117
        self.mask = pygame.mask.from_surface(self.image)
        self.bottom = HEIGHT
        self.add(all_sprites)
        self.add(fon_group)


class AreaY2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(areaG)
        self.image = pygame.image.load('data/fon/second_back.png')
        self.rect = self.image.get_rect()
        self.rect.x = -215
        self.rect.y = 117
        self.mask = pygame.mask.from_surface(self.image)
        self.bottom = HEIGHT
        self.add(all_sprites)
        self.add(fon_group)
