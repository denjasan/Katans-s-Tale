import pygame
from random import randint, choice

from Enemy import *
from Constants import *


class Levels:
    def __init__(self):
        self.level = L01()


class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(laser_group)
        self.image = load_image(choice(("laser1.png", "laser2.png", "laser3.png")))
        self.rect = self.image.get_rect()
        self.rect.x = randint(LASER[0], LASER[1])
        self.rect.y = 409
        self.time = 0

    def update(self, fps):
        if self.time >= fps // 2:
            self.time = 0
            # self.rect.x = randint(LASER[0], LASER[1])
        self.time += 1


class L01:
    def __init__(self):
        self.girl = Enemy(GIRL, x=334, y=330, hp=100)
        self.lasers = []
        for i in range(20):
            a = Laser()
            self.lasers.append((a.rect.x, a.rect.y))

    def render(self):
        self.girl.render()

    def applying(self, camera, player):
        camera.apply(enemy_group, player, self.girl.start_pos)
        for i in range(20):
            camera.apply(laser_group, player, many_strart_poses=self.lasers)

