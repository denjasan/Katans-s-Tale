import pygame

from groups import *
from Constants import *


class Area(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(areaG)
        self.image = pygame.image.load('data/fon/first_back.png')
        self.rect = self.image.get_rect()
        self.rect = [0, 0]
        self.mask = pygame.mask.from_surface(self.image)
        self.bottom = HEIGHT
        self.add(all_sprites)

