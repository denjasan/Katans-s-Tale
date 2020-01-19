import pygame

from Constants import *
from groups import *
from functions import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, player):
        super().__init__(player_group)
        self.player = player
        self.stand_images = []
        self.run_images = []
        self.sword_images = []
        self.dance_images = []
        if self.player == GIRL:
            size = (GIRL_HEIGHT, GIRL_WIDTH)
            self.image = pygame.image.load('data/Girl/PlayingWithBehemot/PlayingWithBehemoth-0.gif')
            self.image = pygame.transform.scale(self.image, size)

            self.stand_images.append(all_pics(G_PLAY, STANDING, size))
            self.stand_images.append(all_pics(G_PLAY, STANDING, size))

            self.run_images.append(all_pics(G_PLAY, RUNNING, size))
            self.run_images.append(all_pics(G_PLAY, RUNNING, size))

            self.sword_images.append(all_pics(G_PLAY, SWORDING_YES, (145, 91)))
            self.sword_images.append(all_pics(G_PLAY, SWORDING_YES, (145, 91)))

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

        self.mask = pygame.mask.from_surface(self.image)

        #self.add(all_sprites)

    def update(self, area, area_x, stairs_del=False):

        if not pygame.sprite.collide_mask(self, area):
            self.rect = self.rect.move(0, self.gravity)

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
        elif self.situation == SWORDING_YES:
            images, move_flag, move = self.go_render(self.sword_images, self.situation, False, SWORD)
        elif self.situation == DANCING:
            images = self.go_render(self.dance_images, self.situation)[0]

        if not move_flag:
            self.anim_count = self.anime(images, move_flag, self.anim_count, move)
        else:
            self.anim_count = self.anime(images, move_flag, self.anim_count)

    def anime(self, images, move_flag, anim_count, move=None):
        if anim_count >= (self.situation - 1) and move_flag:
            anim_count = 0

        if anim_count < self.situation - 1:
            self.image = images[self.direction][anim_count]
            anim_count += 1
        else:
            self.rect.y += 22
            self.rect.x += 40
            self.moving[move] = False
            self.first_time = True
            self.gravity = GRAVITY

        return anim_count


