import pygame

from Constants import *
from groups import *
from functions import *

pygame.init()
size = width, height = 600, 95
screen = pygame.display.set_mode(size)
pygame.display.flip()


class Enemy(pygame.sprite.Sprite):
    image = load_image("Girl/PlayingWithBehemot/GirlPlayingWithBehemoth-0.png")

    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
        super().__init__(group)
        self.image = Enemy.image
        self.rect = self.image.get_rect()
        self.rect.x = 334
        self.rect.y = 330
        self.image = pygame.transform.scale(self.image, (50, 40))


