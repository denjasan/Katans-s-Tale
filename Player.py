import pygame
from Constants import *
from groups import *


class Player(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__(player_group, all_sprites)
        # self.image = player_image
        self.name = name
        self.state = ALIVE
        self.x = START_X
        self.y = START_Y
        self.hp = MAX_HP
        self.direction = RIGHT
        self.mooving = [0, 0]

        self.run = all_sprites()

        pos_x = pos_y = 0
        # self.rect = self.image.get_rect().move(100, 375)

    def update(self, x, mountain):
        pass
        # self.rect.x += x
        # if not pygame.sprite.collide_mask(self, mountain):
        #     self.rect = self.rect.move(0, 1)

    def moove(self):
        """ the movement of the player """
        if self.mooving[RIGHT] == 1:
            self.direction = RIGHT
            self.x += PLAYER_SPEED
        if self.mooving[LEFT] == 1:
            self.direction = LEFT
            self.x -= PLAYER_SPEED

    def render(self, screen, area):
        """ rendering player """
        screen.blit(self.i)
        # player_group.update(self.x, area)
        # self.x = 0
        # player_group.draw(screen)



