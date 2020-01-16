import pygame

from Constants import *
from groups import *
from functions import *


class Player(pygame.sprite.Sprite):
    def __init__(self, name, player):
        super().__init__(all_sprites)
        self.player = player
        self.stand_images = []
        self.run_images = []
        self.sword_images = []
        if self.player == ZERO:
            self.image = pygame.image.load('data/Zero/StandR/0.gif')
            self.image = pygame.transform.scale(self.image, (30, 25))

            self.stand_images.append(all_pics(STANDL, STAND))
            self.stand_images.append(all_pics(STANDR, STAND))

            self.run_images.append(all_pics(RUNL, RUN))
            self.run_images.append(all_pics(RUNR, RUN))

            self.sword_images.append(all_pics(SWORDL, SWORD))
            self.sword_images.append(all_pics(SWORDR, SWORD))

        self.rect = self.image.get_rect()
        self.rect.x = START_X
        self.rect.y = START_Y

        self.situation = STANDING
        self.name = name
        self.state = ALIVE
        self.hp = MAX_HP
        self.direction = RIGHT
        self.mooving = [0, 0]
        self.anim_count = 0

        self.mask = pygame.mask.from_surface(self.image)

        self.add(all_sprites)

    def update(self, area):
        if not pygame.sprite.collide_mask(self, area):
            self.rect = self.rect.move(0, 5)
        # if self.mask.overlap_area(area.mask, offset) > 0:
        # self.rect.x += x
        # if not pygame.sprite.collide_mask(self, mountain):
        #     self.rect = self.rect.move(0, 1)

    def moove(self):
        """ the movement of the player """

        if self.mooving[RIGHT] == self.mooving[LEFT]:
            self.situation = STANDING

        if self.mooving[RIGHT] == 1:
            self.situation = RUNNING
            self.direction = RIGHT
            self.rect.x += PLAYER_SPEED
        if self.mooving[LEFT] == 1:
            self.situation = RUNNING
            self.direction = LEFT
            self.rect.x -= PLAYER_SPEED

    def render(self):
        """ rendering player """
        if self.situation == RUNNING:
            images = self.run_images
        elif self.situation == STANDING:
            images = self.stand_images
        elif self.situation == SWORDING:
            images = self.sword_images

        if self.direction == RIGHT:
            if self.anim_count >= self.situation - 1:
                self.anim_count = 0

            self.image = images[RIGHT][self.anim_count]
            self.anim_count += 1

        elif self.direction == LEFT:
            if self.anim_count >= self.situation - 1:
                self.anim_count = 0

            self.image = images[LEFT][self.anim_count]
            self.anim_count += 1

        # player_group.update(self.x, area)
        # self.x = 0
        # player_group.draw(screen)



