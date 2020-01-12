import pygame
from groups import *


class Area(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(tiles_group)
        self.image = pygame.image.load('data/fon/first_back.png')
        self.rect = [0, 0]
        self.mask = pygame.mask.from_surface(self.image)