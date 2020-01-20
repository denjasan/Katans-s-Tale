import pygame

from Constants import *
from groups import *
from functions import *

# pygame.init()
# size = width, height = 600, 95
# screen = pygame.display.set_mode(size)
# pygame.display.flip()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy, x, y):
        super().__init__(enemy_group, all_sprites)

        if enemy == GIRL:
            self.image = pygame.image.load("data/Girl/GirlPlayingWithBehemoth/0.gif")
            self.image = pygame.transform.scale(self.image, (50, 40))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.start_pos = (x, y)

        self.add(all_sprites)


