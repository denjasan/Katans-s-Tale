import pygame
from Constants import *
from groups import *


class Player(pygame.sprite.Sprite):
    def __init__(self, name, player_image):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.name = name
        self.state = ALIVE
        self.x = START_X
        self.y = START_Y
        self.hp = MAX_HP
        pos_x = pos_y = 0
        self.rect = self.image.get_rect().move(0, 0)

    def move(self):
        """ the movement of the player """
        pass

    def render(self):
        """ rendering player """
        pass



