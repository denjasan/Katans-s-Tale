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
            size = (ZERO_HEIGHT, ZERO_WIDTH)
            self.image = pygame.image.load('data/Zero/StandR/0.gif')
            self.image = pygame.transform.scale(self.image, size)

            self.stand_images.append(all_pics(STANDL, STANDING, size))
            self.stand_images.append(all_pics(STANDR, STANDING, size))

            self.run_images.append(all_pics(RUNL, RUNNING, size))
            self.run_images.append(all_pics(RUNR, RUNNING, size))

            self.sword_images.append(all_pics(SWORDL, SWORDING, (145, 91)))
            self.sword_images.append(all_pics(SWORDR, SWORDING, (145, 91)))

            self.dance_images.append(all_pics(DANCER, DANCING, size))

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
        self.first_time = True
        self.gravity = GRAVITY
        self.last_sender = None
        self.mini_game = False

        self.mask = pygame.mask.from_surface(self.image)

        #self.add(all_sprites)

    def update(self, area_y=None, area_x=None, stairs_del=False, enemy=None):

        if area_y and not pygame.sprite.collide_mask(self, area_y):
            self.rect = self.rect.move(0, self.gravity)

        # if self.situation == SWORDING_YES and self.anim_count == 15:
        #     print(1)
        #     self.mini_game = True
        #     self.anim_count = 0

        if pygame.sprite.spritecollideany(self, enemy_group):
            self.mini_game = True

        if area_x and pygame.sprite.collide_mask(self, area_x):

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
        if self.moving[RIGHT] == self.moving[LEFT] and not any(self.moving[2:]):
            self.situation = STANDING
            self.fps = FPS // 2

        else:

            if self.moving[RIGHT] and not any(self.moving[2:]):
                self.fps = FPS
                self.situation = RUNNING
                self.direction = RIGHT
                self.rect.x += self.speed
            # print(not any(self.moving[3:]), self.moving[3:])
            if self.moving[LEFT] and not any(self.moving[2:]):
                self.fps = FPS
                self.situation = RUNNING
                self.direction = LEFT
                self.rect.x -= self.speed
            if self.moving[SWORD]:
                self.fps = FPS // 2
                if self.first_time:
                    self.rect.y -= 22
                    self.rect.x -= 40
                    self.gravity = 0
                    self.first_time = False
                if self.situation != SWORDING_YES:
                    self.situation = SWORDING
            elif self.moving[DANCE]:
                self.fps = FPS // 2
                self.direction = LEFT
                self.situation = DANCING

    def go_render(self, images, sender, move_flag=True, move=None):
        s = images
        flag = move_flag
        if self.last_sender != sender:
            self.anim_count = 0
        self.last_sender = sender
        return s, flag, move

    def render(self):
        """ rendering player """

        images = []
        move_flag = True
        if self.situation == RUNNING:
            images = self.go_render(self.run_images, self.situation)[0]
        elif self.situation == STANDING:
            images = self.go_render(self.stand_images, self.situation)[0]
        elif self.situation == SWORDING or self.situation == SWORDING_YES:
            images, move_flag, move = self.go_render(self.sword_images, self.situation, False, SWORD)
        elif self.situation == DANCING:
            images = self.go_render(self.dance_images, self.situation)[0]

        if not move_flag:
            self.anim_count = self.anime(images, move_flag, self.anim_count, move)
        else:
            self.anim_count = self.anime(images, move_flag, self.anim_count)

    def anime(self, images, move_flag, anim_count, move=None):
        if anim_count > (self.situation - 1) and move_flag:
            anim_count = 0

        # print(anim_count)

        if anim_count > self.situation - 1:
            self.moving[move] = False
            self.first_time = True
            self.gravity = GRAVITY
            self.rect.y += 22
            self.rect.x += 40
        else:
            self.image = images[self.direction][anim_count]
            anim_count += 1

        # if anim_count <= self.situation - 1:
        #     self.image = images[self.direction][anim_count]
        #     anim_count += 1
        # else:
        #     self.rect.y += 22
        #     self.rect.x += 40
        #     self.moving[move] = False
        #     self.first_time = True
        #     self.gravity = GRAVITY

        return anim_count


