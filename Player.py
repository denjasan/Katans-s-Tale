import pygame

from Constants import *
from groups import *
from functions import *


class Player(pygame.sprite.Sprite):
    def __init__(self, name, player):
        super().__init__(player_group)
        self.player = player
        self.stand_images = []
        self.run_images = []
        self.sword_images = []
        self.dance_images = []
        if self.player == ZERO:
            self.image = pygame.image.load('data/Zero/StandR/0.gif')
            self.image = pygame.transform.scale(self.image, (ZERO_HEIGHT, ZERO_WIDTH))

            self.stand_images.append(all_pics(STANDL, STANDING))
            self.stand_images.append(all_pics(STANDR, STANDING))

            self.run_images.append(all_pics(RUNL, RUNNING))
            self.run_images.append(all_pics(RUNR, RUNNING))

            self.sword_images.append(all_pics(SWORDL, SWORDING_YES))
            self.sword_images.append(all_pics(SWORDR, SWORDING_YES))

            self.dance_images.append(all_pics(DANCER, DANCING))

        self.rect = self.image.get_rect()
        self.rect.x = START_X
        self.rect.y = START_Y

        self.situation = STANDING
        self.name = name
        self.state = ALIVE
        self.hp = MAX_HP
        self.direction = RIGHT
        self.moving = [False, False, False, False, False]
        self.anim_count = 0
        self.speed = PLAYER_SPEED
        self.fps = FPS

        self.mask = pygame.mask.from_surface(self.image)

        #self.add(all_sprites)

    def update(self, area, area_x, stairs_del=False):

        if not pygame.sprite.collide_mask(self, area):
            self.rect = self.rect.move(0, 5)

        if pygame.sprite.collide_mask(self, area_x):

            flag = False

            if not stairs_del:
                for i in STAIRS:
                    if i[0] <= self.rect.x <= i[1]:
                        where = i[2]
                        flag = True
                        break

            # If we are moving right,
            # set our right side to the left side of the item we hit
            if flag and self.moving[RIGHT]:
                if self.direction == where:
                    self.rect.y -= STAIRS_HEIGHT
                # else:
                #     self.rect.y += STAIRS_HEIGHT
            if flag and self.moving[LEFT]:
                print(self.direction, where)
                if self.direction == where:
                    self.rect.y -= STAIRS_HEIGHT
                # else:
                #     self.rect.y += STAIRS_HEIGHT

            if self.moving[RIGHT]:
                self.rect.x = self.rect.x - self.speed
            if self.moving[LEFT]:
                # Otherwise if we are moving left, do the opposite.
                self.rect.x = self.rect.x + self.speed

        # See if we hit anything
        # block_hit_list = pygame.sprite.spritecollide(self, areaG, False)
        # for block in block_hit_list:
        #     # If we are moving right,
        #     # set our right side to the left side of the item we hit
        #     if self.moving[RIGHT] == 1:
        #         self.rect.right = block.rect.left
        #     if self.moving[LEFT] == 1:
        #         # Otherwise if we are moving left, do the opposite.
        #         self.rect.left = block.rect.right
        # if self.mask.overlap_area(area.mask, offset) > 0:
        # self.rect.x += x
        # if not pygame.sprite.collide_mask(self, mountain):
        #     self.rect = self.rect.move(0, 1)

    def move(self):
        """ the movement of the player """
        if self.moving[RIGHT] == self.moving[LEFT] and not any(self.moving[3:]):
            self.situation = STANDING
            self.fps = FPS // 2

        else:

            if self.moving[RIGHT] and not any(self.moving[3:]):
                self.fps = FPS
                self.situation = RUNNING
                self.direction = RIGHT
                self.rect.x += self.speed
            # print(not any(self.moving[3:]), self.moving[3:])
            if self.moving[LEFT] and not any(self.moving[3:]):
                self.fps = FPS
                self.situation = RUNNING
                self.direction = LEFT
                self.rect.x -= self.speed
            if self.moving[DANCE]:
                self.fps = FPS // 2
                self.direction = LEFT
                self.situation = DANCING

    def render(self):
        """ rendering player """

        images = []
        if self.situation == RUNNING:
            images = self.run_images
        elif self.situation == STANDING:
            images = self.stand_images
        elif self.situation == SWORDING_YES:
            images = self.sword_images
        elif self.situation == DANCING:
            images = self.dance_images

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



