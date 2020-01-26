import pygame

from Constants import *
from groups import *
from functions import *

# pygame.init()
# size = width, height = 600, 95
# screen = pygame.display.set_mode(size)
# pygame.display.flip()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy, x, y, hp):
        super().__init__(enemy_group)

        self.stand_images = []
        self.run_images = []
        self.sword_images = []
        self.dance_images = []
        if enemy == GIRL:
            size = (GIRL_HEIGHT, GIRL_WIDTH)
            self.image = pygame.image.load("data/Girl/GirlPlayingWithBehemoth/0.gif")
            self.image = pygame.transform.scale(self.image, size)
            self.name = 'Girl'
            self.situation = G_PLAYING

            self.stand_images.append(all_pics(G_PLAY, G_PLAYING, size))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.start_pos = (x, y)
        self.state = ALIVE
        self.hp = hp
        self.direction = LEFT
        self.moving = [False, False, False, False, False]
        self.anim_count = 0
        self.speed = PLAYER_SPEED
        self.fps = FPS
        self.first_time = True
        self.gravity = GRAVITY
        self.last_sender = None

        self.mask = pygame.mask.from_surface(self.image)

        # self.add(all_sprites)

    def update(self, player, situation):
        if situation == SWORDING and pygame.sprite.collide_mask(self, player):
            # print('et')
            player.situation = SWORDING_YES

    def go_render(self, images, sender, move_flag=True, move=None):
        s = images
        flag = move_flag
        if self.last_sender != sender:
            self.anim_count = 0
        self.last_sender = sender
        return s, flag, move

    def render(self):
        """ rendering player """
        # print(1)
        images = []
        move_flag = True
        if self.situation == RUNNING:
            images = self.go_render(self.run_images, self.situation)[0]
        elif self.situation == G_PLAYING:
            images = self.go_render(self.stand_images, self.situation)[0]
        # print(images)
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
        return anim_count


